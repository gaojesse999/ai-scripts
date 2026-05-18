// Treatment — .docx generator (LEGACY)
//
// Default skill output is Markdown (`templates/treatment.template.md` + `markdown-style.md`).
// Use this script only when the user explicitly asks for a `.docx` file.
//
// Each scene = a heading + 3-5 sentences of description.
// Optional — audit tags: ⚠ [CAUSALITY] / [VALUE] / [BIBLE] / [PACE]
//
// Usage:
//   1. Copy the file into your working folder.
//   2. Fill in the `treatment` array via scene("Title", "Body").
//   3. NODE_PATH=/usr/local/lib/node_modules_global/lib/node_modules node build_treatment.js

const fs = require("fs");
const docx = require("docx");
const {
  Document, Packer, Paragraph, TextRun,
  AlignmentType, HeadingLevel, Header, PageNumber
} = docx;

const FONT = "Calibri";
const SIZE = 22; // 11pt

// Localize the scene-heading prefix as needed: "Scene", "Сцена", "场景", etc.
const SCENE_LABEL = "Scene";

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
      new TextRun({ text: `${SCENE_LABEL} ${_sceneNum}. `, font: FONT, size: SIZE, bold: true }),
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

// ============ TREATMENT ============

const treatment = [
  new Paragraph({
    spacing: { after: 240 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "PROJECT TITLE", font: FONT, size: 44, bold: true })]
  }),
  new Paragraph({
    spacing: { after: 480 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "Treatment v1", font: FONT, size: 24, italics: true })]
  }),

  act("Act I"),

  ...scene(
    "Location — Time — State",
    "3-5 sentences: what happens, who is present, which value enters, which action plays out, which value exits. Concrete action verbs, no emotion descriptions."
  ),

  ...scene(
    "Next scene",
    "An audit tag can sit here if there's a structural issue.",
    "[CAUSALITY] This scene does not follow from the previous — needs a bridge."
  ),

  // Add your scenes below.
  // Use act("Act II"), act("Act III") for dividers.
];

// ============ BUILD ============

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
