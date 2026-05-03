#!/usr/bin/env dotnet run

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

// Parse arguments (args is already available in top-level statements)
if (args.Length == 0 || args.Contains("-h") || args.Contains("--help"))
{
    PrintHelp();
    return;
}

var url = args[0];
var outputDir = GetArgValue(args, "-o", "--output") ?? ".";
var fpsStr = GetArgValue(args, "--fps"); // null means auto-detect based on duration
var fpsExplicit = fpsStr != null;
if (fpsStr == null) fpsStr = "1.0"; // default, may be overridden after API call
if (!double.TryParse(fpsStr, NumberStyles.Float, CultureInfo.InvariantCulture, out var fps))
{
    Console.WriteLine($"[ERROR] Invalid fps value: {fpsStr}");
    Environment.Exit(1);
}
var similarityStr = GetArgValue(args, "--similarity") ?? "0.65";
if (!double.TryParse(similarityStr, NumberStyles.Float, CultureInfo.InvariantCulture, out var similarityThreshold))
{
    Console.WriteLine($"[ERROR] Invalid similarity value: {similarityStr}");
    Environment.Exit(1);
}
var videoOnly = args.Contains("--video-only");
var framesOnly = args.Contains("--frames-only");
var noDedup = args.Contains("--no-dedup");

var videoPath = Path.Combine(outputDir, "video.mp4");
var imagesRawDir = Path.Combine(outputDir, "images_raw");
var imagesDir = Path.Combine(outputDir, "images");

// Create output directory
Directory.CreateDirectory(outputDir);

Console.WriteLine(new string('=', 50));
Console.WriteLine("Bilibili Video Analyzer - Prepare Script");
Console.WriteLine(new string('=', 50));
Console.WriteLine($"URL: {url}");
Console.WriteLine($"Output: {outputDir}");
Console.WriteLine($"FPS: {fps}{(fpsExplicit ? "" : " (auto, may change after fetching video info)")}");
Console.WriteLine($"Similarity Threshold: {similarityThreshold:P0}");
Console.WriteLine($"Deduplication: {(noDedup ? "Disabled" : "Enabled")}");
Console.WriteLine(new string('=', 50));

// Download video
if (!framesOnly)
{
    if (!await DownloadBilibiliVideoAsync(url, videoPath))
    {
        Environment.Exit(1);
    }
}

// Extract frames
if (!videoOnly)
{
    if (!File.Exists(videoPath))
    {
        Console.WriteLine($"[ERROR] Video file not found: {videoPath}");
        Environment.Exit(1);
    }

    // Clean up old data before extraction to prevent stale frame residue
    CleanDirectory(imagesRawDir);
    CleanDirectory(imagesDir);

    if (!await ExtractFramesAsync(videoPath, imagesRawDir, fps))
    {
        Environment.Exit(1);
    }

    // Deduplicate similar frames: read from images_raw/, write kept frames to images/
    if (!noDedup)
    {
        await DeduplicateFramesAsync(imagesRawDir, imagesDir, similarityThreshold);
    }
    else
    {
        // No dedup: copy all frames from images_raw/ to images/
        await CopyAllFramesAsync(imagesRawDir, imagesDir);
    }
}

Console.WriteLine();
Console.WriteLine(new string('=', 50));
Console.WriteLine("[OK] Done!");
Console.WriteLine($"  Video: {videoPath}");
Console.WriteLine($"  Raw frames: {imagesRawDir}/");
Console.WriteLine($"  Deduped images: {imagesDir}/");
Console.WriteLine(new string('=', 50));

// === Functions ===

void CleanDirectory(string dir)
{
    if (Directory.Exists(dir))
    {
        var oldFiles = Directory.GetFiles(dir, "frame_*.jpg");
        if (oldFiles.Length > 0)
        {
            Console.WriteLine($"[INFO] Cleaning {oldFiles.Length} old frames from {dir}/");
            foreach (var file in oldFiles)
            {
                try { File.Delete(file); } catch { }
            }
        }
    }
}

async Task<bool> DownloadBilibiliVideoAsync(string url, string outputPath)
{
    Console.WriteLine($"[INFO] Downloading video: {url}");

    try
    {
        // Extract BV ID and page number from URL
        var bvid = ExtractBvid(url);
        if (string.IsNullOrEmpty(bvid))
        {
            Console.WriteLine("[ERROR] Invalid Bilibili URL, cannot extract BV ID");
            return false;
        }
        var pageNum = ExtractPageNumber(url); // p=N parameter, default 1
        Console.WriteLine($"[INFO] BV ID: {bvid}");
        if (pageNum > 1)
            Console.WriteLine($"[INFO] Page: P{pageNum}");

        using var client = CreateHttpClient();

        // Step 1: Get video info to obtain cid
        Console.WriteLine("[INFO] Fetching video info...");
        var infoUrl = $"https://api.bilibili.com/x/web-interface/view?bvid={bvid}";
        var infoJson = await client.GetStringAsync(infoUrl);
        using var infoDoc = JsonDocument.Parse(infoJson);

        var code = infoDoc.RootElement.GetProperty("code").GetInt32();
        if (code != 0)
        {
            var message = infoDoc.RootElement.GetProperty("message").GetString();
            Console.WriteLine($"[ERROR] Failed to get video info: {message}");
            return false;
        }

        var data = infoDoc.RootElement.GetProperty("data");
        var title = data.GetProperty("title").GetString();
        var totalDuration = data.GetProperty("duration").GetInt64();
        var selectedDuration = totalDuration;

        // Resolve cid: use pages array for multi-part videos
        long cid;
        if (data.TryGetProperty("pages", out var pages) && pages.GetArrayLength() > 0)
        {
            if (pageNum > pages.GetArrayLength())
            {
                Console.WriteLine($"[ERROR] Page P{pageNum} not found, video has {pages.GetArrayLength()} pages");
                return false;
            }
            var page = pages[pageNum - 1]; // 0-indexed
            cid = page.GetProperty("cid").GetInt64();
            if (page.TryGetProperty("part", out var partName))
                Console.WriteLine($"[INFO] Part: {partName.GetString()}");
            if (page.TryGetProperty("duration", out var pageDuration))
                selectedDuration = pageDuration.GetInt64();
        }
        else
        {
            cid = data.GetProperty("cid").GetInt64();
        }

        Console.WriteLine($"[INFO] Title: {title}");
        if (selectedDuration != totalDuration)
        {
            Console.WriteLine($"[INFO] Total BV duration: {totalDuration}s ({totalDuration / 60.0:F1} min)");
            Console.WriteLine($"[INFO] Selected page duration: {selectedDuration}s ({selectedDuration / 60.0:F1} min)");
        }
        else
        {
            Console.WriteLine($"[INFO] Duration: {selectedDuration}s ({selectedDuration / 60.0:F1} min)");
        }

        if (!fpsExplicit)
        {
            // Auto-select fps based on the selected page duration, not the whole BV duration
            if (selectedDuration < 600)        fps = 1.0;   // <10 min
            else if (selectedDuration < 1800)  fps = 0.5;   // 10-30 min
            else                               fps = 0.2;   // >30 min
            Console.WriteLine($"[INFO] Auto-selected fps={fps} based on selected duration");
        }
        Console.WriteLine($"[INFO] CID: {cid}");

        // Step 2: Get playback URL
        Console.WriteLine("[INFO] Fetching playback URL...");
        var playUrl = $"https://api.bilibili.com/x/player/playurl?bvid={bvid}&cid={cid}&qn=80&fnval=1";
        var playJson = await client.GetStringAsync(playUrl);
        using var playDoc = JsonDocument.Parse(playJson);

        var playCode = playDoc.RootElement.GetProperty("code").GetInt32();
        if (playCode != 0)
        {
            var message = playDoc.RootElement.GetProperty("message").GetString();
            Console.WriteLine($"[ERROR] Failed to get playback URL: {message}");
            return false;
        }

        var playData = playDoc.RootElement.GetProperty("data");
        var durl = playData.GetProperty("durl")[0];
        var videoUrl = durl.GetProperty("url").GetString();
        var size = durl.GetProperty("size").GetInt64();
        var candidateUrls = new List<string>();

        if (!string.IsNullOrWhiteSpace(videoUrl))
            candidateUrls.Add(videoUrl);

        if (durl.TryGetProperty("backup_url", out var backupUrls) && backupUrls.ValueKind == JsonValueKind.Array)
        {
            foreach (var backup in backupUrls.EnumerateArray())
            {
                var backupUrl = backup.GetString();
                if (!string.IsNullOrWhiteSpace(backupUrl) && !candidateUrls.Contains(backupUrl, StringComparer.Ordinal))
                    candidateUrls.Add(backupUrl);
            }
        }

        if (candidateUrls.Count == 0)
        {
            Console.WriteLine("[ERROR] No playable video URL returned by Bilibili API");
            return false;
        }

        Console.WriteLine($"[INFO] Video size: {size / 1024.0 / 1024.0:F1} MB");
        Console.WriteLine($"[INFO] Candidate download URLs: {candidateUrls.Count}");

        // Step 3: Download video
        Console.WriteLine("[INFO] Downloading video file...");

        if (!await DownloadFileWithResumeAsync(client, candidateUrls, $"https://www.bilibili.com/video/{bvid}", outputPath, size))
        {
            return false;
        }

        Console.WriteLine($"[OK] Video downloaded: {outputPath}");
        return true;
    }
    catch (HttpRequestException ex)
    {
        Console.WriteLine($"[ERROR] Network error: {ex.Message}");
        return false;
    }
    catch (JsonException ex)
    {
        Console.WriteLine($"[ERROR] Failed to parse API response: {ex.Message}");
        return false;
    }
    catch (Exception ex)
    {
        Console.WriteLine($"[ERROR] Download failed: {ex.Message}");
        return false;
    }
}

async Task<bool> DownloadFileWithResumeAsync(HttpClient client, IReadOnlyList<string> candidateUrls, string referer, string outputPath, long expectedSize)
{
    const int maxAttempts = 12;
    var buffer = new byte[81920];
    string? lastError = null;

    if (File.Exists(outputPath) && expectedSize > 0)
    {
        var existingSize = new FileInfo(outputPath).Length;
        if (existingSize == expectedSize)
        {
            Console.WriteLine("[INFO] Existing video.mp4 already matches expected size, skipping download");
            Console.WriteLine("[INFO] Progress: 100%");
            return true;
        }

        if (existingSize > expectedSize)
        {
            Console.WriteLine("[WARN] Existing video.mp4 is larger than expected size, restarting download");
            File.Delete(outputPath);
        }
    }

    for (int attempt = 1; attempt <= maxAttempts; attempt++)
    {
        var url = candidateUrls[(attempt - 1) % candidateUrls.Count];
        var fileLength = File.Exists(outputPath) ? new FileInfo(outputPath).Length : 0L;

        if (expectedSize > 0 && fileLength == expectedSize)
        {
            Console.WriteLine("[INFO] Progress: 100%");
            return true;
        }

        try
        {
            Console.WriteLine($"[INFO] Download attempt {attempt}/{maxAttempts} {(fileLength > 0 ? $"(resuming from {fileLength / 1024.0 / 1024.0:F1} MB)" : "")}");
            if (attempt > 1 || candidateUrls.Count > 1)
            {
                Console.WriteLine($"[INFO] Source URL #{((attempt - 1) % candidateUrls.Count) + 1}");
            }

            using var request = new HttpRequestMessage(HttpMethod.Get, url);
            request.Headers.Referrer = new Uri(referer);
            request.Version = HttpVersion.Version11;
            request.VersionPolicy = HttpVersionPolicy.RequestVersionOrLower;

            if (fileLength > 0)
            {
                request.Headers.Range = new RangeHeaderValue(fileLength, null);
            }

            using var response = await client.SendAsync(request, HttpCompletionOption.ResponseHeadersRead);

            if (fileLength > 0 && response.StatusCode == HttpStatusCode.RequestedRangeNotSatisfiable)
            {
                if (expectedSize > 0 && fileLength >= expectedSize)
                {
                    Console.WriteLine("[INFO] Server reported full file already present locally");
                    Console.WriteLine("[INFO] Progress: 100%");
                    return true;
                }

                Console.WriteLine("[WARN] Server rejected resume range, restarting from byte 0");
                File.Delete(outputPath);
                fileLength = 0;
                continue;
            }

            response.EnsureSuccessStatusCode();

            var resumeAccepted = fileLength == 0 || response.StatusCode == HttpStatusCode.PartialContent;
            if (!resumeAccepted && fileLength > 0)
            {
                Console.WriteLine("[WARN] Server ignored resume request, restarting full download");
                File.Delete(outputPath);
                fileLength = 0;
            }

            var totalBytes = expectedSize > 0 ? expectedSize : (response.Content.Headers.ContentLength ?? 0) + fileLength;
            if (totalBytes <= 0)
            {
                totalBytes = 1;
            }

            await using var contentStream = await response.Content.ReadAsStreamAsync();
            await using var fileStream = new FileStream(
                outputPath,
                fileLength > 0 ? FileMode.Append : FileMode.Create,
                FileAccess.Write,
                FileShare.None,
                buffer.Length,
                true);

            var totalRead = fileLength;
            var lastProgress = totalBytes > 0 ? (int)(totalRead * 100 / totalBytes) : -1;
            if (lastProgress >= 10 && lastProgress < 100)
            {
                Console.WriteLine($"[INFO] Progress: {lastProgress}%");
            }

            int bytesRead;
            while ((bytesRead = await contentStream.ReadAsync(buffer)) > 0)
            {
                await fileStream.WriteAsync(buffer.AsMemory(0, bytesRead));
                totalRead += bytesRead;

                var progress = (int)(totalRead * 100 / totalBytes);
                if (progress != lastProgress && (progress % 10 == 0 || progress == 100))
                {
                    Console.WriteLine($"[INFO] Progress: {progress}%");
                    lastProgress = progress;
                }
            }

            if (expectedSize > 0 && totalRead < expectedSize)
            {
                throw new IOException($"The response ended prematurely, with at least {expectedSize - totalRead} additional bytes expected.");
            }

            if (lastProgress != 100)
            {
                Console.WriteLine("[INFO] Progress: 100%");
            }

            return true;
        }
        catch (Exception ex) when (attempt < maxAttempts)
        {
            lastError = ex.Message;
            Console.WriteLine($"[WARN] Download attempt {attempt} failed: {ex.Message}");
            await Task.Delay(TimeSpan.FromSeconds(Math.Min(attempt, 5)));
        }
        catch (Exception ex)
        {
            lastError = ex.Message;
            break;
        }
    }

    Console.WriteLine($"[ERROR] Download failed after {maxAttempts} attempts: {lastError}");
    return false;
}

string? ExtractBvid(string url)
{
    // Match BV ID from various URL formats
    // https://www.bilibili.com/video/BV1xx411c7mD
    // https://www.bilibili.com/video/BV1xx411c7mD?p=1
    // https://b23.tv/BV1xx411c7mD
    // BV1xx411c7mD
    // BV ID is exactly 12 characters: BV + 10 alphanumeric chars
    var match = Regex.Match(url, @"BV[a-zA-Z0-9]{10}");
    return match.Success ? match.Value : null;
}

int ExtractPageNumber(string url)
{
    // Extract p=N parameter from URL query string
    // https://www.bilibili.com/video/BV1xx411c7mD?p=4 → 4
    var match = Regex.Match(url, @"[?&]p=(\d+)");
    if (match.Success && int.TryParse(match.Groups[1].Value, out var page) && page > 0)
        return page;
    return 1; // default to first page
}

HttpClient CreateHttpClient()
{
    var handler = new HttpClientHandler
    {
        AutomaticDecompression = System.Net.DecompressionMethods.GZip | System.Net.DecompressionMethods.Deflate
    };

    var client = new HttpClient(handler);
    client.DefaultRequestHeaders.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36");
    client.DefaultRequestHeaders.Add("Referer", "https://www.bilibili.com");
    client.DefaultRequestHeaders.Add("Accept", "application/json, text/plain, */*");
    client.Timeout = TimeSpan.FromMinutes(30);

    return client;
}

async Task<bool> ExtractFramesAsync(string videoPath, string outputDir, double fps)
{
    Console.WriteLine($"[INFO] Extracting frames (fps={fps})");

    var ffmpeg = FindExecutable("ffmpeg", "ffmpeg.exe");
    if (ffmpeg == null)
    {
        Console.WriteLine("[ERROR] ffmpeg not found!");
        Console.WriteLine("        Windows: choco install ffmpeg / scoop install ffmpeg");
        Console.WriteLine("        macOS: brew install ffmpeg");
        Console.WriteLine("        Linux: sudo apt install ffmpeg");
        return false;
    }

    Directory.CreateDirectory(outputDir);
    var outputPattern = Path.Combine(outputDir, "frame_%04d.jpg");

    try
    {
        Console.WriteLine($"[INFO] Running ffmpeg: {ffmpeg}");

        var psi = new ProcessStartInfo
        {
            FileName = ffmpeg,
            Arguments = $"-i \"{videoPath}\" -vf \"fps={fps.ToString(CultureInfo.InvariantCulture)}\" -q:v 2 -y \"{outputPattern}\"",
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
            CreateNoWindow = true
        };

        using var process = Process.Start(psi);
        if (process == null)
        {
            Console.WriteLine("[ERROR] Failed to start ffmpeg");
            return false;
        }

        // Read stderr asynchronously to prevent deadlock
        var stderrTask = process.StandardError.ReadToEndAsync();
        await process.WaitForExitAsync();
        var stderr = await stderrTask;

        // ffmpeg returns 0 on success, non-zero on failure
        if (process.ExitCode != 0)
        {
            // Only show last few lines of error
            var errorLines = stderr.Split('\n').TakeLast(5);
            Console.WriteLine($"[ERROR] Frame extraction failed (exit code {process.ExitCode}):");
            foreach (var line in errorLines)
            {
                if (!string.IsNullOrWhiteSpace(line))
                    Console.WriteLine($"        {line.Trim()}");
            }
            return false;
        }

        var frameCount = Directory.GetFiles(outputDir, "frame_*.jpg").Length;
        if (frameCount == 0)
        {
            Console.WriteLine("[ERROR] No frames extracted. Check if video file is valid.");
            return false;
        }

        Console.WriteLine($"[OK] Frames extracted: {frameCount} images saved to {outputDir}/");
        return true;
    }
    catch (Exception ex)
    {
        Console.WriteLine($"[ERROR] Frame extraction failed: {ex.Message}");
        return false;
    }
}

async Task CopyAllFramesAsync(string sourceDir, string destDir)
{
    Console.WriteLine($"[INFO] Copying all frames from {sourceDir}/ to {destDir}/ (no dedup)...");
    Directory.CreateDirectory(destDir);

    var files = Directory.GetFiles(sourceDir, "frame_*.jpg")
        .OrderBy(f => f)
        .ToList();

    var manifest = new List<DedupManifestEntry>();
    for (int i = 0; i < files.Count; i++)
    {
        var destFile = Path.Combine(destDir, $"frame_{i + 1:D4}.jpg");
        File.Copy(files[i], destFile, overwrite: true);
        manifest.Add(new DedupManifestEntry
        {
            RawFrame = Path.GetFileName(files[i]),
            RawIndex = i + 1,
            OutputFrame = $"frame_{i + 1:D4}.jpg",
            OutputIndex = i + 1
        });
    }

    // Write manifest
    var manifestObj = new DedupManifest
    {
        DeduplicationEnabled = false,
        SimilarityThreshold = 0.0,
        RawDirectory = "images_raw",
        OutputDirectory = "images",
        RawFrameCount = files.Count,
        OutputFrameCount = files.Count,
        KeptFrames = manifest
    };
    var manifestJson = JsonSerializer.Serialize(manifestObj, BilibiliAnalyzerJsonContext.Default.DedupManifest);
    await File.WriteAllTextAsync(Path.Combine(Path.GetDirectoryName(destDir)!, "dedup_manifest.json"), manifestJson);

    Console.WriteLine($"[OK] Copied {files.Count} frames to {destDir}/");
}

async Task DeduplicateFramesAsync(string rawDir, string outputDir, double threshold)
{
    Console.WriteLine($"[INFO] Deduplicating similar frames (threshold: {threshold:P0})...");
    Console.WriteLine($"[INFO] Reading from: {rawDir}/");
    Console.WriteLine($"[INFO] Writing to: {outputDir}/");

    Directory.CreateDirectory(outputDir);

    var files = Directory.GetFiles(rawDir, "frame_*.jpg")
        .OrderBy(f => f)
        .ToList();

    if (files.Count < 2)
    {
        Console.WriteLine("[INFO] Not enough frames to deduplicate");
        // Copy all to output
        for (int i = 0; i < files.Count; i++)
        {
            File.Copy(files[i], Path.Combine(outputDir, $"frame_{i + 1:D4}.jpg"), overwrite: true);
        }
        return;
    }

    var toRemoveIndices = new HashSet<int>();
    var ffmpeg = FindExecutable("ffmpeg", "ffmpeg.exe");

    if (ffmpeg == null)
    {
        Console.WriteLine("[WARN] ffmpeg not found, skipping deduplication");
        await CopyAllFramesAsync(rawDir, outputDir);
        return;
    }

    // Compare each frame against the last KEPT frame (not just the previous frame)
    // This ensures cascading dedup: if frames 1,2,3,4,5 are all similar, only frame 1 is kept
    var lastKeptIndex = 0; // Index of the last frame we decided to keep
    for (int i = 1; i < files.Count; i++)
    {
        var similarity = await CalculateFrameSimilarityAsync(ffmpeg, files[lastKeptIndex], files[i]);

        if (similarity >= threshold)
        {
            // Similar to last kept frame → remove this one
            toRemoveIndices.Add(i);
        }
        else
        {
            // Different enough → keep this one, update reference
            lastKeptIndex = i;
        }
    }

    // Copy kept frames to output directory with sequential numbering
    var manifest = new List<DedupManifestEntry>();
    var outputIndex = 0;
    for (int i = 0; i < files.Count; i++)
    {
        if (toRemoveIndices.Contains(i))
            continue;

        outputIndex++;
        var outputFile = Path.Combine(outputDir, $"frame_{outputIndex:D4}.jpg");
        File.Copy(files[i], outputFile, overwrite: true);
        manifest.Add(new DedupManifestEntry
        {
            RawFrame = Path.GetFileName(files[i]),
            RawIndex = i + 1,
            OutputFrame = $"frame_{outputIndex:D4}.jpg",
            OutputIndex = outputIndex
        });
    }

    // Write dedup_manifest.json
    var manifestObj = new DedupManifest
    {
        DeduplicationEnabled = true,
        SimilarityThreshold = threshold,
        RawDirectory = "images_raw",
        OutputDirectory = "images",
        RawFrameCount = files.Count,
        OutputFrameCount = outputIndex,
        KeptFrames = manifest
    };
    var manifestJson = JsonSerializer.Serialize(manifestObj, BilibiliAnalyzerJsonContext.Default.DedupManifest);
    await File.WriteAllTextAsync(Path.Combine(Path.GetDirectoryName(outputDir)!, "dedup_manifest.json"), manifestJson);

    Console.WriteLine($"[OK] Deduplication complete: {files.Count} -> {outputIndex} frames (removed {toRemoveIndices.Count} similar frames)");
    Console.WriteLine($"[OK] Manifest saved: dedup_manifest.json");
}

async Task<double> CalculateFrameSimilarityAsync(string ffmpeg, string file1, string file2)
{
    try
    {
        // Use ffmpeg to calculate PSNR (Peak Signal-to-Noise Ratio) between two images
        // Higher PSNR = more similar images
        var psi = new ProcessStartInfo
        {
            FileName = ffmpeg,
            Arguments = $"-i \"{file1}\" -i \"{file2}\" -lavfi \"psnr\" -f null -",
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
            CreateNoWindow = true
        };

        using var process = Process.Start(psi);
        if (process == null) return 0;

        var stderrTask = process.StandardError.ReadToEndAsync();
        await process.WaitForExitAsync();
        var stderr = await stderrTask;

        // Parse PSNR value from output
        // Format: [Parsed_psnr_0 @ ...] PSNR y:XX.XX u:XX.XX v:XX.XX average:XX.XX min:XX.XX max:XX.XX
        var match = Regex.Match(stderr, @"average:(\d+\.?\d*)", RegexOptions.IgnoreCase);
        if (match.Success && double.TryParse(match.Groups[1].Value, NumberStyles.Float, CultureInfo.InvariantCulture, out var psnr))
        {
            // Convert PSNR to similarity percentage
            // PSNR > 40 dB is considered very similar (>95%)
            // PSNR > 30 dB is considered similar (>80%)
            // PSNR = infinity means identical images
            if (psnr > 100) return 1.0; // Identical or near-identical
            if (psnr > 40) return 0.95 + (psnr - 40) * 0.001;
            if (psnr > 30) return 0.80 + (psnr - 30) * 0.015;
            if (psnr > 20) return 0.50 + (psnr - 20) * 0.03;
            return psnr * 0.025;
        }

        // Fallback: use simpler SSIM if PSNR parsing fails
        return await CalculateSSIMAsync(ffmpeg, file1, file2);
    }
    catch
    {
        return 0;
    }
}

async Task<double> CalculateSSIMAsync(string ffmpeg, string file1, string file2)
{
    try
    {
        var psi = new ProcessStartInfo
        {
            FileName = ffmpeg,
            Arguments = $"-i \"{file1}\" -i \"{file2}\" -lavfi \"ssim\" -f null -",
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
            CreateNoWindow = true
        };

        using var process = Process.Start(psi);
        if (process == null) return 0;

        var stderrTask = process.StandardError.ReadToEndAsync();
        await process.WaitForExitAsync();
        var stderr = await stderrTask;

        // Parse SSIM value: All:0.XXXXX
        var match = Regex.Match(stderr, @"All:(\d+\.?\d*)", RegexOptions.IgnoreCase);
        if (match.Success && double.TryParse(match.Groups[1].Value, NumberStyles.Float, CultureInfo.InvariantCulture, out var ssim))
        {
            return ssim; // SSIM is already 0-1 range
        }

        return 0;
    }
    catch
    {
        return 0;
    }
}

string? FindExecutable(params string[] names)
{
    var pathEnv = Environment.GetEnvironmentVariable("PATH") ?? "";
    var paths = pathEnv.Split(Path.PathSeparator);

    foreach (var name in names)
    {
        foreach (var path in paths)
        {
            try
            {
                var fullPath = Path.Combine(path, name);
                if (File.Exists(fullPath)) return fullPath;
            }
            catch { } // Ignore invalid paths
        }
    }

    // Common Windows paths
    if (OperatingSystem.IsWindows())
    {
        var commonPaths = new[]
        {
            @"C:\ffmpeg\bin",
            @"C:\Program Files\ffmpeg\bin",
            @"C:\tools\ffmpeg\bin",
            Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), "scoop", "shims"),
            Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "Microsoft", "WinGet", "Links"),
        };

        foreach (var basePath in commonPaths)
        {
            foreach (var name in names)
            {
                try
                {
                    var fullPath = Path.Combine(basePath, name);
                    if (File.Exists(fullPath)) return fullPath;
                }
                catch { }
            }
        }
    }

    // Try where/which command
    try
    {
        var cmd = OperatingSystem.IsWindows() ? "where" : "which";
        var psi = new ProcessStartInfo
        {
            FileName = cmd,
            Arguments = names[0],
            RedirectStandardOutput = true,
            UseShellExecute = false,
            CreateNoWindow = true
        };
        using var process = Process.Start(psi);
        if (process != null)
        {
            process.WaitForExit(5000); // 5 second timeout
            var output = process.StandardOutput.ReadToEnd()?.Trim();
            if (!string.IsNullOrEmpty(output))
            {
                var firstLine = output.Split('\n')[0].Trim();
                if (File.Exists(firstLine)) return firstLine;
            }
        }
    }
    catch { }

    return null;
}

string? GetArgValue(string[] args, params string[] names)
{
    for (int i = 0; i < args.Length - 1; i++)
    {
        if (names.Contains(args[i]))
        {
            return args[i + 1];
        }
    }
    return null;
}

void PrintHelp()
{
    Console.WriteLine(@"
Bilibili Video Analyzer - Prepare Script

Usage:
        From the skill root:
            dotnet run scripts/prepare.cs -- <url> [options]

        From any directory:
            dotnet run <path-to-skill>/scripts/prepare.cs -- <url> [options]

Arguments:
  url                    Bilibili video URL (required)
                         Supports multi-part videos: ...?p=4

Options:
  -o, --output <dir>     Output directory (default: current)
  --fps <value>          Frames per second (auto if omitted:
                           <10min: 1.0, 10-30min: 0.5, >30min: 0.2)
  --similarity <value>   Similarity threshold for deduplication (default: 0.65)
  --no-dedup             Disable frame deduplication (still copies to images/)
  --video-only           Only download video, skip frame extraction
    --frames-only          Only extract frames (requires existing video.mp4;
                                                     pass --fps explicitly because auto fps is only
                                                     available when video metadata is fetched)
  -h, --help             Show this help

Output Structure:
  <output>/video.mp4              Downloaded video
  <output>/images_raw/            All extracted frames (raw)
  <output>/images/                Deduplicated frames (for analysis)
  <output>/dedup_manifest.json    Raw-to-output frame mapping

Examples:
    cd <skill-root>
    dotnet run scripts/prepare.cs -- ""https://www.bilibili.com/video/BV1xx411c7mD"" -o ./output
    dotnet run scripts/prepare.cs -- ""https://www.bilibili.com/video/BV1xx411c7mD?p=4"" -o ./output
    dotnet run scripts/prepare.cs -- ""https://www.bilibili.com/video/BV1xx411c7mD"" -o ./output --fps 0.5
    dotnet run scripts/prepare.cs -- dummy-url -o ./output --frames-only --fps 0.5

Deduplication:
  Each frame is compared against the last kept frame.
  Consecutive similar frames are fully collapsed (only the first is kept).
  Uses ffmpeg SSIM/PSNR for accurate similarity calculation.

Download robustness:
    The downloader uses HTTP/1.1, resume, retry, and backup_url fallback for
    Bilibili CDN interruptions.

Requirements:
  - .NET 10 SDK
  - ffmpeg: https://ffmpeg.org/download.html
");
}

sealed class DedupManifest
{
        [JsonPropertyName("deduplicationEnabled")]
        public bool DeduplicationEnabled { get; init; }

        [JsonPropertyName("similarityThreshold")]
        public double SimilarityThreshold { get; init; }

        [JsonPropertyName("rawDirectory")]
        public string RawDirectory { get; init; } = "images_raw";

        [JsonPropertyName("outputDirectory")]
        public string OutputDirectory { get; init; } = "images";

        [JsonPropertyName("rawFrameCount")]
        public int RawFrameCount { get; init; }

        [JsonPropertyName("outputFrameCount")]
        public int OutputFrameCount { get; init; }

        [JsonPropertyName("keptFrames")]
        public List<DedupManifestEntry> KeptFrames { get; init; } = new();
}

sealed class DedupManifestEntry
{
        [JsonPropertyName("rawFrame")]
        public string RawFrame { get; init; } = "";

        [JsonPropertyName("rawIndex")]
        public int RawIndex { get; init; }

        [JsonPropertyName("outputFrame")]
        public string OutputFrame { get; init; } = "";

        [JsonPropertyName("outputIndex")]
        public int OutputIndex { get; init; }
}

[JsonSourceGenerationOptions(WriteIndented = true)]
[JsonSerializable(typeof(DedupManifest))]
internal partial class BilibiliAnalyzerJsonContext : JsonSerializerContext
{
}
