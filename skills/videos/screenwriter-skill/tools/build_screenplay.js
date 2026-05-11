// Hollywood-формат сценария — генератор .docx
//
// Использование:
//   1. Скопируй этот файл в свою рабочую папку, переименуй (например, build_my_scene.js).
//   2. Внутри массива `screenplay` напиши свои сцены через helpers (slug/action/character/dial и т.д.).
//   3. Запусти: NODE_PATH=/usr/local/lib/node_modules_global/lib/node_modules node build_my_scene.js
//   4. Получишь screenplay.docx в той же папке.
//
// Hollywood-формат:
//   Page 8.5" x 11" (US Letter)
//   Margins: top 1", bottom 1", left 1.5", right 1"
//   Courier New 12pt (равноширинный → 1 страница ≈ 1 минута экрана при смешанном диалог/экшен)
//   Slug-line: ALL CAPS bold, левое поле
//   Action: левое поле, present tense
//   Character cue: indent 2.2" (3168 DXA)
//   Parenthetical: indent 1.6" (2304 DXA)
//   Dialogue: indent 1" left + 1.5" right (1440 / 2160 DXA)
//   Transition: правое поле, ALL CAPS

const fs = require("fs");
const docx = require("docx");
const {
  Document, Packer, Paragraph, TextRun,
  AlignmentType, Header, PageNumber, PageBreak
} = docx;

const FONT = "Courier New";
const SIZE = 24; // 12pt в half-points

// ============ HELPERS ============

// Включи автонумерацию сцен. Установи стартовый номер если блок начинается не с 1.
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
    indent: { left: 3168 }, // 2.2"
    keepNext: true,
    children: [new TextRun({ text: txt, font: FONT, size: SIZE })]
  });
}

function paren(t) {
  return new Paragraph({
    spacing: { before: 0, after: 0, line: 240 },
    indent: { left: 2304, right: 2880 }, // 1.6" left, ~2.0" right
    keepNext: true,
    children: [new TextRun({ text: t.startsWith("(") ? t : `(${t})`, font: FONT, size: SIZE })]
  });
}

function dial(t) {
  return new Paragraph({
    spacing: { before: 0, after: 0, line: 240 },
    indent: { left: 1440, right: 2160 }, // 1" left, 1.5" right
    children: [new TextRun({ text: t, font: FONT, size: SIZE })]
  });
}

function trans(t) {
  return new Paragraph({
    spacing: { before: 240, after: 240, line: 240 },
    alignment: AlignmentType.RIGHT,
    children: [new TextRun({ text: t.toUpperCase(), font: FONT, size: SIZE, bold: true })]
  });
}

function pageBreak() { return new Paragraph({ children: [new PageBreak()] }); }
function blank() { return new Paragraph({ spacing: { before: 0, after: 0, line: 240 }, children: [new TextRun({ text: "", font: FONT, size: SIZE })] }); }

function center(t, opts = {}) {
  return new Paragraph({
    spacing: { before: opts.before ?? 240, after: opts.after ?? 240, line: 240 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: t, font: FONT, size: opts.size || SIZE, bold: !!opts.bold })]
  });
}

// ============ ВАШИ СЦЕНЫ ============

const screenplay = [
  blank(), blank(),
  center("MY PROJECT", { bold: true, size: 32 }),
  center("Scene Block — Working Title"),
  blank(),

  // Пример сцены — замени на свои.
  slug("EXT. ЛОКАЦИЯ — ВРЕМЯ СУТОК"),
  action("Описание того, что видно в кадре. Только глаголы действия."),
  action("Второе действие, если нужно."),

  character("ГЕРОЙ"),
  dial("Реплика героя."),

  character("ВТОРОЙ ПЕРСОНАЖ"),
  paren("тихо"),
  dial("Реплика второго."),

  trans("CUT TO:"),

  // Добавляй свои сцены ниже.
];

// ============ СБОРКА ============

const doc = new Document({
  creator: "Screenwriter",
  title: "Screenplay",
  styles: { default: { document: { run: { font: FONT, size: SIZE } } } },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 }, // 8.5" x 11"
        margin: { top: 1440, right: 1440, bottom: 1440, left: 2160 } // 1.5" left, 1" else
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
  const out = "./screenplay.docx";
  fs.writeFileSync(out, buf);
  console.log(`wrote ${out}`);
}).catch(e => { console.error(e); process.exit(1); });
