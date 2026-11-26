# Task: write model exam answers (Anna University CS3551 Distributed Computing, R2021)

You are writing the answer script of a top-scoring student for ONE part of "Model Question Paper 1".
The answers will be printed as an answer booklet that students copy from, so they must be
**technically correct**, complete, and written the way a student writes in the exam hall.

## How to write (exam answer-script style)
- Start each answer by restating what is given / to prove in one line ("Given: … To prove: …") when useful.
- Theory answers: start with an **Introduction / Definition**, then the main body under clear sub-headings, then a short **Conclusion**.
- Algorithms: write **System model & assumptions**, **Data structures / message types**, **Algorithm steps** (numbered), a **diagram** (space-time diagram, wait-for graph, or block diagram), a short **worked example**, **Correctness / properties**, and **Performance** (message complexity, synchronization delay) where relevant.
- Comparisons: use a comparison table (`<table class="tt">`) with at least 5 rows.
- Case-study questions: restate the scenario, give the recommended choice with a diagram, justify it point by point, compare with alternatives, conclude.
- Follow the standard textbooks: Kshemkalyani & Singhal, "Distributed Computing: Principles, Algorithms and Systems" (Units I–IV) and Bahga & Madisetti, "Cloud Computing: A Hands-On Approach" (Unit V). Use their terminology, algorithm names and message names.
- Use clear sub-headings inside an answer (h4). Short paragraphs. No chatty text, no "As an AI".
- Examiners reward: definitions, neat diagrams, step-by-step working, and a clear final result. Include all of these.
- Length guide (handwritten exam pages, about 120 words per page):
  - 2-mark answer: 4–8 lines (40–90 words), or a small table.
  - 13-mark answer: about 4–5 pages (500–650 words) plus 1–3 diagrams/tables.
  - 15-mark answer (Part C): about 5–6 pages (600–750 words) plus diagrams.
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
  Arrows: define `<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#000"/></marker></defs>` once per SVG and use `marker-end="url(#ar)"` on lines.
  Space-time diagrams: one horizontal line per process (label P1, P2 … on the left), time flows left to right, events as dots, messages as slanted arrows from sender event to receiver event, labels near the arrows.
  Never put HTML tags such as <sub> inside SVG <text>; write P1, C1, m1 as plain text or use <tspan baseline-shift="sub" font-size="10">.
  Block / architecture diagrams: rectangles `<rect fill="none" stroke="#000">` with centred text, arrows between them.

## Accuracy
- Double-check every algorithm step, message name, condition and complexity figure against the textbook before writing the file.
- After writing the file, re-read it once and fix any mistake.
