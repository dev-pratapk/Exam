# Anna University previous year papers and pattern analysis

| Subject | Analysis PDF | Folder |
|---|---|---|
| MA3354 Discrete Mathematics | [PDF](MA3354_Exam_Pattern_Analysis.pdf) | this page (below) |
| CS3551 Distributed Computing | [PDF](CS3551-Distributed-Computing/CS3551_Exam_Pattern_Analysis.pdf) | [CS3551-Distributed-Computing/](CS3551-Distributed-Computing/) |

---

# MA3354 Discrete Mathematics: Previous Year Papers and Pattern Analysis

Anna University · B.E./B.Tech · Regulation 2021, 3rd semester

**Download the analysis PDF: [MA3354_Exam_Pattern_Analysis.pdf](MA3354_Exam_Pattern_Analysis.pdf)**

**Model question papers (exact exam format): [MA3354_Model_Question_Papers.pdf](MA3354_Model_Question_Papers.pdf)**. These are three full papers laid out like the real Anna University paper (Part A 10 × 2, Part B 5 × 16 with (a) Or (b)). Every question is a real question from a previous paper:
- Paper 1: the most-repeated questions.
- Paper 2: the next most frequent questions.
- Paper 3: "due" topics and R2021-style questions.

The last page lists where each question came from.

**Answer booklets for Model Question Paper 1.** Two complete model answer scripts, written the way you write in the exam hall:
- [Booklet A](answer-booklets/MA3354_Model_Paper_1_Answer_Booklet_A.pdf): Part A (all 10) and option (a) of Q11–Q15.
- [Booklet B](answer-booklets/MA3354_Model_Paper_1_Answer_Booklet_B.pdf): Part A (all 10) and option (b) of Q11–Q15.

Each booklet has a cover sheet listing the questions answered. Every answer shows how many handwritten pages it should take: about 30–35 pages in total, so you do not need to fill all 42 pages. The diagrams are included.

The answers were drafted by the DeepSeek V4.1 Flash model, run through [opencode](https://opencode.ai), and then checked step by step. Every numerical result was recomputed, and every diagram's edge list was compared with its question. Still, check the answers against your textbook before memorising them. The prompts and raw answers are in `answer-booklets/source/`.

It has:
- the most-repeated questions,
- a priority list of what to study first,
- a unit-wise bank of every Part B question from 14 past papers,
- Part A (2-mark) patterns.

## What was found

- Anna University reuses questions. Whole papers come back. For example, 2016 May/June and 2017 April/May are almost the same paper. Single questions also cross regulations: `(¬P ∧ (¬Q ∧ R)) ∨ (Q ∧ R) ∨ (P ∧ R) ⇔ R` appeared in 2016, 2018, 2023 and 2024.
- Each Part B question has an (a) OR (b) choice. Learning the **top 10 skills** in the PDF would have given at least **48/80 in Part B in every one of the 14 papers**, with an average of 62/80.
- The method was also tested on unseen papers. A study list built only from the 2016–2021 papers was checked against the 2022–2024 R2021 papers. It scored at least 48/80 in each of them.

The PDF explains the method step by step. No one can guarantee a question paper: use this to prioritise, not to skip units.

## Question papers

The earlier subjects MA6566 (R2013) and MA8351 (R2017) cover the same five units as MA3354, so their papers are included too. Only the question pages are kept.

| Session | Regulation | Subject | QP code | File |
|---|---|---|---|---|
| 2024 April/May | R2021 | MA3354 | 51325 | [PDF](question-papers/R2021_MA3354/MA3354_2024_Apr-May_QP51325.pdf) |
| 2023 Nov/Dec | R2021 | MA3354 | 21282 | [PDF](question-papers/R2021_MA3354/MA3354_2023_Nov-Dec_QP21282.pdf) |
| 2023 April/May | R2021 | MA3354 | 30243 | [PDF](question-papers/R2021_MA3354/MA3354_2023_Apr-May_QP30243.pdf) |
| 2022 Nov/Dec | R2021 | MA3354 | 70141 | [PDF](question-papers/R2021_MA3354/MA3354_2022_Nov-Dec_QP70141.pdf) |
| 2021 Nov/Dec | R2017 | MA8351 | 40784 | [PDF](question-papers/R2017_MA8351/MA8351_2021_Nov-Dec_QP40784.pdf) |
| 2020 Nov/Dec | R2017 | MA8351 | X10657 | [PDF](question-papers/R2017_MA8351/MA8351_2020_Nov-Dec_QPX10657.pdf) |
| 2019 Nov/Dec | R2017 | MA8351 | 90336 | [PDF](question-papers/R2017_MA8351/MA8351_2019_Nov-Dec_QP90336.pdf) |
| 2019 April/May | R2017 | MA8351 | 80212 | [PDF](question-papers/R2017_MA8351/MA8351_2019_Apr-May_QP80212.pdf) |
| 2018 Nov/Dec | R2017 | MA8351 | 25139 | [PDF](question-papers/R2017_MA8351/MA8351_2018_Nov-Dec_QP25139.pdf) |
| 2018 April/May | R2013 | MA6566 | 41320 | [PDF](question-papers/R2013_MA6566/MA6566_2018_Apr-May_QP41320.pdf) |
| 2017 Nov/Dec | R2013 | MA6566 | 50789 | [PDF](question-papers/R2013_MA6566/MA6566_2017_Nov-Dec_QP50789.pdf) |
| 2017 April/May | R2013 | MA6566 | 72078 | [PDF](question-papers/R2013_MA6566/MA6566_2017_Apr-May_QP72078.pdf) |
| 2016 Nov/Dec | R2013 | MA6566 | 80615 | [PDF](question-papers/R2013_MA6566/MA6566_2016_Nov-Dec_QP80615.pdf) |
| 2016 May/June | R2013 | MA6566 | 57517 | [PDF](question-papers/R2013_MA6566/MA6566_2016_May-Jun_QP57517.pdf) |

**Missing papers:** Nov/Dec 2024, Apr/May 2025, Nov/Dec 2025 and Apr/May 2026. If you have any of these, please open an issue or a pull request, and the analysis will be updated.

## Re-running the analysis

- `analysis/papers.py`: every Part B sub-question of the 14 papers, tagged with the skill it needs and its marks.
- `python3 analysis/run.py`: shows how often each skill appears, and the backtest (how many Part B marks a study list would have scored in each paper).
- `python3 analysis/validate.py`: the out-of-sample test, where old papers predict the R2021 papers.
- `REPO_URL=https://github.com/<owner>/<repo> report/build.sh`: rebuilds the analysis PDF (needs Python 3 and Node with Playwright).
- `model-papers/build.sh`: rebuilds the model question papers. The questions are in `model-papers/build_model.py`; figures are cropped from the original papers.

## Credits

Fonts: Noto Sans and Noto Sans Math (SIL Open Font License), in `report/fonts/`.

The question papers are Anna University end-semester papers, collected from student sites (Brainkart, EnggTree). This project is unofficial and not affiliated with Anna University. Free to share for studying.
