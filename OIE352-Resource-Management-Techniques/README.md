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

## Question papers (CS6704, Regulations 2013)

| Session | QP code | File |
|---|---|---|
| 2021 Nov/Dec | 70398 | [PDF](question-papers/R2013_CS6704/CS6704_2021_Nov-Dec_QP70398.pdf) |
| 2020 Nov/Dec | X20411 | [PDF](question-papers/R2013_CS6704/CS6704_2020_Nov-Dec_QPX20411.pdf) |

**If you have OIE352 papers** (Nov/Dec 2024 onwards), please open an issue or a pull request and the analysis will be redone.

## Re-running
- `python3 analysis/run.py` shows topic frequency and the cross-check.
- `report/build.sh` rebuilds the PDF.

Unofficial; not affiliated with Anna University.
