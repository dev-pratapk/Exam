# CS3551 Distributed Computing: Previous Year Papers and Pattern Analysis

Anna University · Regulation 2021 · Semester 5

**Download the analysis PDF: [CS3551_Exam_Pattern_Analysis.pdf](CS3551_Exam_Pattern_Analysis.pdf)**

**Model question papers (exact exam format): [CS3551_Model_Question_Papers.pdf](CS3551_Model_Question_Papers.pdf)**. Two full papers laid out like the real Anna University paper: Part A 10 × 2, Part B 5 × 13 with (a) Or (b), and Part C 1 × 15 with (a) Or (b). Every question is a real question from a previous paper:
- Paper 1: the most-repeated questions.
- Paper 2: the next most frequent questions.

The last page lists which paper each question came from.

**Answer booklets for Model Question Paper 1.** Two complete answer scripts, written the way you write in the exam hall:
- [Booklet A](answer-booklets/CS3551_Model_Paper_1_Answer_Booklet_A.pdf): Part A (all 10), and option (a) of Q11–Q16.
- [Booklet B](answer-booklets/CS3551_Model_Paper_1_Answer_Booklet_B.pdf): Part A (all 10), and option (b) of Q11–Q16.

Each booklet has a cover sheet listing the questions answered. Every answer shows how many handwritten pages it should take: about 30–36 pages in total, so you do not need to fill all 42. Algorithm answers include space-time diagrams and worked examples.

Some answers were drafted by the free DeepSeek model (through [opencode](https://opencode.ai)) and the rest written with Claude; all were checked against the textbook algorithms. See `answer-booklets/source/README.md`. Check the answers against your own textbook before memorising them.

It contains the top 15 topics to study (3 per unit) and every question from the past papers grouped by topic. It also explains the Part C case-study pattern and how the analysis was done.

## What was found
- **Paper format:** Part A has 10 × 2 marks. Part B has 5 × 13 marks, one question per unit with an (a) OR (b) choice. Part C has 1 × 15 marks, (a) OR (b), usually a case study.
- **Unit II is the heaviest unit.** Logical clocks came in all 6 papers. The snapshot / global-state algorithm and message ordering each came in 5 of 6.
- **Questions repeat in every CS3551 paper:** Chandy–Misra–Haas, cloud services, issues in failure recovery, and virtualization or cloud characteristics.
- **Studying 3 topics per unit (15 topics) is enough to cover Part B + Part C.** In a leave-one-out test, a 15-topic list built from the other papers scored 80, 80 and 67 out of 80 on the hidden CS3551 papers. Two topics per unit was not enough (39–67).

Only 6 papers exist so far, so the patterns are less certain than for older subjects. Use this to prioritise, not to skip units.

## Question papers

| Session | Subject | QP code | File |
|---|---|---|---|
| 2024 Nov/Dec | CS3551 (R2021) | 40927 | [PDF](question-papers/R2021_CS3551/CS3551_2024_Nov-Dec_QP40927.pdf) |
| 2024 April/May | CS3551 (R2021) | 50907 | [PDF](question-papers/R2021_CS3551/CS3551_2024_Apr-May_QP50907.pdf) |
| 2023 Nov/Dec | CS3551 (R2021) | 20874 | [PDF](question-papers/R2021_CS3551/CS3551_2023_Nov-Dec_QP20874.pdf) |
| 2023 Nov/Dec | CS8603 (R2017) | 12155 | [PDF](question-papers/R2017_CS8603/CS8603_2023_Nov-Dec_QP12155.pdf) |
| 2021 Nov/Dec | CS8603 (R2017) | 40400 | [PDF](question-papers/R2017_CS8603/CS8603_2021_Nov-Dec_QP40400.pdf) |
| 2021 April/May | CS8603 (R2017) | X10324 | [PDF](question-papers/R2017_CS8603/CS8603_2021_Apr-May_QPX10324.pdf) |

CS8603 Distributed Systems (R2017) shares Units I–IV with CS3551. Its Unit V (P2P and distributed shared memory) is not in CS3551, so those questions are left out of the counts.

**Missing:** April/May 2025, Nov/Dec 2025 and April/May 2026. They are on Studocu / Scribd behind logins. If you have them, please open an issue or a pull request.

## Re-running
- `python3 analysis/run.py` shows topic frequency.
- `python3 analysis/validate.py` runs the leave-one-out test.
- `report/build.sh` rebuilds the analysis PDF.
- `model-papers/build.sh` rebuilds the model question papers. The questions are in `model-papers/build_model.py`.

Unofficial; not affiliated with Anna University.
