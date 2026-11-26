# OIE352 Resource Management Techniques: Pattern Analysis

Anna University · Regulation 2021 · Open Elective II

**Download the analysis PDF: [OIE352_Exam_Pattern_Analysis.pdf](OIE352_Exam_Pattern_Analysis.pdf)**

## Important: there are no public OIE352 papers yet
EnggTree lists the OIE352 papers as "Coming Soon", Brainkart has none, and the Anna University library site could not be reached. So this analysis uses the two public papers of **CS6704 Resource Management Techniques** (Regulations 2013), the same subject: the same five units and the same textbook (Taha). Two papers give an indication, not proof.

## What was found
- The subject is **problem solving**: simplex, dual simplex, transportation, assignment, integer LP, dynamic programming, Kuhn–Tucker, CPM and PERT.
- **Part C was the same two problems in both papers**: unbalanced transportation (maximize the profit of five salesmen in four places) and an integer programming problem (Maximize Z = 80x₁ + 45x₂; optimum 420 at x₁ = 3, x₂ = 4).
- Dual simplex (Q12a), Kuhn–Tucker (Q14), CPM and PERT (Q15) and LP graphical (Q11) came in both papers.
- Studying the top 2 problem types per unit from one paper covered all 80 marks of the other paper (a consistency check on two papers).
- Two printing errors: 2020 Q13(a) prints "2x₁ = 11" (intended ≤ 11) and 2021 Part C prints 600 where 60 is intended.

## Model question papers and answer booklets

**Model question papers (exam format): [OIE352_Model_Question_Papers.pdf](OIE352_Model_Question_Papers.pdf).** Two papers laid out like the real paper (Part A 10 × 2, Part B 5 × 13 with (a) Or (b), Part C 1 × 15 with (a) Or (b)). Every question is a real question of the two CS6704 papers; the last page shows which paper each came from. The real OIE352 paper may differ.

**Answer booklets for Model Question Paper 1:**
- [Booklet A](answer-booklets/OIE352_Model_Paper_1_Answer_Booklet_A.pdf): Part A (all 10) and option (a) of Q11–Q16.
- [Booklet B](answer-booklets/OIE352_Model_Paper_1_Answer_Booklet_B.pdf): Part A (all 10) and option (b) of Q11–Q16.

Each booklet has a cover sheet and shows how many handwritten pages each answer should take (about 28–32 pages in total). Every simplex, dual simplex, transportation (VAM + MODI), branch and bound, dynamic programming and PERT table was produced by exact-fraction programs and the results were checked (the transportation and integer-programming answers also by exhaustive search). The graph and the network diagram are drawn to scale. See `answer-booklets/source/README.md`. Check the answers against your own textbook before memorising them.

## Question papers (CS6704, Regulations 2013)

| Session | QP code | File |
|---|---|---|
| 2021 Nov/Dec | 70398 | [PDF](question-papers/R2013_CS6704/CS6704_2021_Nov-Dec_QP70398.pdf) |
| 2020 Nov/Dec | X20411 | [PDF](question-papers/R2013_CS6704/CS6704_2020_Nov-Dec_QPX20411.pdf) |

**If you have OIE352 papers** (Nov/Dec 2024 onwards), please open an issue or a pull request and the analysis will be redone.

## Re-running
- `python3 analysis/run.py` shows topic frequency and the cross-check.
- `report/build.sh` rebuilds the analysis PDF; `model-papers/build.sh` rebuilds the model papers (questions in `model-papers/build_model.py`).

Unofficial; not affiliated with Anna University.
