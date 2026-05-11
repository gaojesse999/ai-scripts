// Поэпизодник (treatment) — генератор .docx
//
// Каждая сцена = заголовок + 3-5 предложений описания.
// Опционально — теги аудита: ⚠ [ПРИЧИННОСТЬ] / [ЦЕННОСТЬ] / [БИБЛИЯ] / [ТЕМП]
//
// Использование:
//   1. Скопируй файл в рабочую папку.
//   2. Заполни массив `treatment` через scene("Заголовок", "Описание").
//   3. NODE_PATH=/usr/local/lib/node_modules_global/lib/node_modules node build_treatment.js

const fs = require("fs");
const docx = require("docx");
const {
  Document, Packer, Paragraph, TextRun,
  AlignmentType, HeadingLevel, Header, PageNumber
} = docx;

const FONT = "Calibri";
const SIZE = 22; // 11pt

let _sceneNum = 0;

function act(title) {
  return new Paragraph({
    spacing: { before: 480, after: 240 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: title.toUpperCase(), font: FONT, size: 32, bold: true })]
  });
}

function scene(title, body, audit) {
  _sceneNum++;
  const titlePara = new Paragraph({
    spacing: { before: 360, after: 60 },
    children: [
      new TextRun({ text: `Сцена ${_sceneNum}. `, font: FONT, size: SIZE, bold: true }),
      new TextRun({ text: title, font: FONT, size: SIZE, bold: true })
    ]
  });
  const bodyPara = new Paragraph({
    spacing: { before: 0, after: 120, line: 280 },
    children: [new TextRun({ text: body, font: FONT, size: SIZE })]
  });
  const out = [titlePara, bodyPara];
  if (audit) {
    out.push(new Paragraph({
      spacing: { before: 0, after: 240, line: 280 },
      children: [new TextRun({ text: `⚠ ${audit}`, font: FONT, size: SIZE - 2, italics: true, color: "C00000" })]
    }));
  }
  return out;
}

// ============ ПОЭПИЗОДНИК ============

const treatment = [
  new Paragraph({
    spacing: { after: 240 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "PROJECT TITLE", font: FONT, size: 44, bold: true })]
  }),
  new Paragraph({
    spacing: { after: 480 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "Поэпизодник v1", font: FONT, size: 24, italics: true })]
  }),

  act("Акт I"),

  ...scene(
    "Локация — Время — Состояние",
    "3-5 предложений: что происходит, кто присутствует, какая ценность входит, какое действие происходит, какая ценность выходит. Конкретные глаголы действия, никаких описаний эмоций."
  ),

  ...scene(
    "Следующая сцена",
    "Здесь может быть тег аудита, если есть проблема в структуре.",
    "[ПРИЧИННОСТЬ] Эта сцена не следует из предыдущей — нужен мост."
  ),

  // Добавляй свои сцены ниже.
  // Используй act("Акт II"), act("Акт III") для разделителей.
];

// ============ СБОРКА ============

const doc = new Document({
  creator: "Screenwriter",
  title: "Treatment",
  styles: { default: { document: { run: { font: FONT, size: SIZE } } } },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 20 })]
        })]
      })
    },
    children: treatment
  }]
});

Packer.toBuffer(doc).then(buf => {
  const out = "./treatment.docx";
  fs.writeFileSync(out, buf);
  console.log(`wrote ${out}`);
}).catch(e => { console.error(e); process.exit(1); });
