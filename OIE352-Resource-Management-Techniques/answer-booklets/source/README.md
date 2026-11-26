# How the OIE352 answer booklets were made

- `solvers.py`: exact-fraction solvers (Big-M simplex, dual simplex, transportation with VAM and MODI) that print the tableaux.
- `gen_answers.py`: writes every answer (text, tables, diagrams). All numbers come from the solvers or are asserted in the script. The transportation and integer-programming results are also checked by exhaustive search (run without `FAST=1`).
- `assemble.py`: builds the two booklets from `answers/`.
- `answers/`: the generated answers as HTML fragments.

The answers were written with Claude. Check the method and notation against your textbook before memorising.
