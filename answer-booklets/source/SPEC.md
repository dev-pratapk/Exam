# Task: write model exam answers (Anna University MA3354 Discrete Mathematics, R2021)

You are writing the answer script of a top-scoring student for ONE part of "Model Question Paper 1".
The answers will be printed as an answer booklet that students copy from, so they must be
**mathematically correct**, complete, and written the way a student writes in the exam hall.

## How to write (exam answer-script style)
- Start each answer by restating what is given / to prove in one line ("Given: … To prove: …") when useful.
- Theorems: write **Statement**, **Definitions used**, **Proof** (numbered steps, each with a reason), then a boxed **Result / Hence proved**.
- Problems: write the formula/method first, then every working step, then the boxed final answer.
- Logic proofs with rules of inference: use a step table with columns Step no. | Statement | Reason (Rule P, Rule T, Rule CP, US, UG, ES, EG, with the step numbers used).
- Use clear sub-headings inside an answer (h4). Short paragraphs. No chatty text, no "As an AI".
- Examiners reward: definitions, neat diagrams, step-by-step working, and a clear final result. Include all of these.
- Length guide (handwritten exam pages, about 120 words per page):
  - 2-mark answer: 4–8 lines (40–90 words), plus a tiny diagram/table if the question needs it.
  - 8-mark answer: about 2.5–3 pages (300–450 words) plus diagrams/tables.
  - 16-mark answer: about 5–6 pages.
  Do NOT pad. Write what earns marks.

## Output format (STRICT)
Write ONLY an HTML fragment (no <html>, <head>, <body>, <style>, <script>, no markdown, no code fences) to the file named in your task.
Use only these elements:
- One wrapper per answer: `<div class="ans" data-q="11 (a) (i)" data-pages="2.5"> … </div>`
  (`data-q` = exact question label; `data-pages` = how many handwritten pages this answer should take in the exam.)
- Inside: `<h4>`, `<p>`, `<ol>`, `<ul>`, `<li>`, `<b>`, `<i>`, `<sub>`, `<sup>`, `<br>`,
  `<table class="tt">` with `<tr><th>/<td>` for truth tables and step tables,
  `<div class="eq">` for a displayed equation/line of working,
  `<div class="result">` for the final boxed answer,
  `<figure class="dg"><svg …>…</svg><figcaption>…</figcaption></figure>` for diagrams.
- Math: plain Unicode (¬ ∧ ∨ → ↔ ⇔ ⇒ ∀ ∃ ∈ ⊆ ≤ ≥ ≠ ≡ √ Σ × ∘ ′) with `<sub>`/`<sup>`. Use * for a group operation.
- Diagrams: inline SVG only, black on white: `<svg width="…" height="…" viewBox="…" xmlns="http://www.w3.org/2000/svg">`,
  lines `stroke="#000" stroke-width="1.6"`, vertices `<circle r="4" fill="#000"/>`, labels `<text font-size="14" font-family="serif">`.
  Keep each SVG ≤ 420 px wide. Make sure every edge you draw matches the text exactly, and labels do not overlap lines.
  Hasse diagrams: bottom element at the bottom, every covering relation drawn as a line going upward, no arrows.

## Accuracy
- Double-check every number, every truth-table row, every degree count and every algebra step before writing the file.
- If the question has more than one correct method, use the standard textbook method (Veerarajan / Rosen / Tremblay–Manohar).
- After writing the file, re-read it once and fix any mistake.
