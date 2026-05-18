// Bilingual screenplay — .docx generator (LEGACY)
//
// Default skill output is Markdown (`markdown-style.md`, "Bilingual" section).
// Use this script only when the user explicitly asks for a `.docx` file.
//
// Each dialogue line = two lines:
//   1. Primary language (e.g., English or Chinese).
//   2. Translation in italic grey parentheses (e.g., the other language).
//
// Action, parentheticals and slug-lines — in the user's chosen language (see constants near helpers).
//
// Usage:
//   1. Copy the file into your working folder.
//   2. Write each dialogue line through ...dialB("primary line", "translation line").
//   3. NODE_PATH=/usr/local/lib/node_modules_global/lib/node_modules node build_bilingual.js

const fs = require("fs");
const docx = require("docx");
const {
  Document, Packer, Paragraph, TextRun,
  AlignmentType, Header, PageNumber
} = docx;

const FONT = "Courier New";
const SIZE = 24;

// ============ HELPERS ============

const ENABLE_SCENE_NUMBERS = true;
const START_SCENE_NUMBER = 1;
let _sceneNum = START_SCENE_NUMBER - 1;

function slug(t) {
  let text = t.toUpperCase();
  if (ENABLE_SCENE_NUMBERS) {
    _sceneNum++;
    text = `${_sceneNum}  ${text}`;
  }
  return new Paragraph({
    spacing: { before: 360, after: 240, line: 240 },
    keepNext: true,
    children: [new TextRun({ text, font: FONT, size: SIZE, bold: true })]
  });
}

function action(t) {
  return new Paragraph({
    spacing: { before: 0, after: 240, line: 240 },
    children: [new TextRun({ text: t, font: FONT, size: SIZE })]
  });
}

function character(name, ext) {
  const txt = ext ? `${name.toUpperCase()} (${ext})` : name.toUpperCase();
  return new Paragraph({
    spacing: { before: 240, after: 0, line: 240 },
    indent: { left: 3168 },
    keepNext: true,
    children: [new TextRun({ text: txt, font: FONT, size: SIZE })]
  });
}

function paren(t) {
  return new Paragraph({
    spacing: { before: 0, after: 0, line: 240 },
    indent: { left: 2304, right: 2880 },
    keepNext: true,
    children: [new TextRun({ text: t.startsWith("(") ? t : `(${t})`, font: FONT, size: SIZE })]
  });
}

function dialMain(t) {
  return new Paragraph({
    spacing: { before: 0, after: 0, line: 240 },
    indent: { left: 1440, right: 2160 },
    children: [new TextRun({ text: t, font: FONT, size: SIZE })]
  });
}

function dialTranslation(t) {
  return new Paragraph({
    spacing: { before: 0, after: 120, line: 240 },
    indent: { left: 1440, right: 2160 },
    children: [new TextRun({ text: `(${t})`, font: FONT, size: SIZE, italics: true, color: "666666" })]
  });
}

// Main bilingual helper: spread it inline — ...dialB("...", "...")
function dialB(main, translation) {
  return [dialMain(main), dialTranslation(translation)];
}

function trans(t) {
  return new Paragraph({
    spacing: { before: 240, after: 240, line: 240 },
    alignment: AlignmentType.RIGHT,
    children: [new TextRun({ text: t.toUpperCase(), font: FONT, size: SIZE, bold: true })]
  });
}

function center(t, opts = {}) {
  return new Paragraph({
    spacing: { before: opts.before ?? 240, after: opts.after ?? 240, line: 240 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: t, font: FONT, size: opts.size || SIZE, bold: !!opts.bold })]
  });
}

function blank() {
  return new Paragraph({ spacing: { before: 0, after: 0, line: 240 }, children: [new TextRun({ text: "", font: FONT, size: SIZE })] });
}

// ============ YOUR SCENES ============

const screenplay = [
  blank(), blank(),
  center("MY PROJECT", { bold: true, size: 32 }),
  center("Bilingual Draft (Primary / Translation)"),
  blank(),

  slug("EXT. LOCATION — DAY"),
  action("Scene description in the primary language. Action verbs only."),

  character("HERO"),
  ...dialB(
    "Primary-language dialogue line.",
    "Translation line in the second language."
  ),

  character("OTHER"),
  paren("quiet"),
  ...dialB(
    "Another line.",
    "Another translation."
  ),

  trans("CUT TO:"),

  // Add your scenes below.
];

// ============ BUILD ============

const doc = new Document({
  creator: "Screenwriter",
  title: "Bilingual Screenplay",
  styles: { default: { document: { run: { font: FONT, size: SIZE } } } },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 2160 }
      }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          children: [new TextRun({ children: [PageNumber.CURRENT, "."], font: FONT, size: 22 })]
        })]
      })
    },
    children: screenplay
  }]
});

Packer.toBuffer(doc).then(buf => {
  const out = "./screenplay-bilingual.docx";
  fs.writeFileSync(out, buf);
  console.log(`wrote ${out}`);
}).catch(e => { console.error(e); process.exit(1); });
