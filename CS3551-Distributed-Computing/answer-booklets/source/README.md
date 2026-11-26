# How the CS3551 answer booklets were made

- `answers/`: one HTML file per answer (the text, tables and SVG diagrams that go into the booklets).
- `assemble.py`: builds the two booklets from the answers (the page layout, cover sheet and page guide).
- `SPEC.md`, `run_jobs.py`, `prompts/`: the instructions and prompts used for the answers drafted by the free DeepSeek V4.1 Flash model, run through [opencode](https://opencode.ai). These are Part A (answers 1–10), 11(a), 11(b), 13(a) and 13(b).
- Answers 12(a), 12(b), 14(a), 14(b), 15(a), 15(b), 16(a) and 16(b) were written with Claude, because the free DeepSeek servers stopped responding.

Every answer was checked against the textbook algorithms (Kshemkalyani and Singhal for Units I–IV, Bahga and Madisetti for Unit V). Corrections made after the DeepSeek drafts include the Send-variant table in 11(a), a complexity claim in 13(b), and the diagrams in 11(a) and 13(a), which were redrawn because labels overlapped.
