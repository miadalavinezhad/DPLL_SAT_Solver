# DPLL SAT Solver
This project solves the satisfiability problem for CNF (Conjuctive Normal Form) by using DPLL (Davis–Putnam–Logemann–Loveland), a backtracking-based algorithm.

## Pseudocode
Here is the pseudocode of the algorithm.
```
dpll(formula):
    while unit clause {q} in formula:
        remove clauses containing 'q'
        omit '¬q' from clauses

    while pure literal 'p' in formula:
        remove clauses containing p

    while superset S in formula:
        remove S

    if formula is empty:
        return True
    if formula containing empty clause:
        return False

    l ← choose_a_literal_from(formula)
    return dpll(formula ʌ {l}) or dpll(formula ʌ {¬l})
```
## How To Use The Code
Call dpll() function and give a list of lists as the argument for the function. The list format should be a list like the example below:
```
cnf = [[1, 2], [-1, 3], [-2, -3], [2, 3]]
dpll(cnf)
```
The list represents a CNF, each list inside represents a clause and each number represents a literal. If the CNF is satisfiable, dpll will return True and a partial assignment and if it's unsatisfiable it returns False with no assignment.

## Example of an input and its output
### Input (SAT)
```
formula = [[1, 2], [-1, 3], [-2, -3], [2, 3]]
```
### Output
```
Assignment:  {}
Start Formula:  [[1, 2], [-1, 3], [-2, -3], [2, 3]]
Cleaning process (1) U.P.:  [[1, 2], [-1, 3], [-2, -3], [2, 3]]
Cleaning process (2) P.L.E.:  [[1, 2], [-1, 3], [-2, -3], [2, 3]]
Cleaning process (3) Superset Elimination:  [[1, 2], [-1, 3], [-3, -2], [2, 3]]
hosen literal:  2
--------------------------------------------
Assignment:  {2: True}
Start Formula:  [[1, 2], [-1, 3], [-3, -2], [2, 3], [2]]
Cleaning process (1) U.P.:  [[-1, 3], [-3]]
Cleaning process (2) P.L.E.:  [[-3]]
Cleaning process (3) Superset Elimination:  [[-3]]
hosen literal:  -3
--------------------------------------------
Assignment:  {2: True, -3: True}
Start Formula:  [[-3]]
Cleaning process (1) U.P.:  []
Cleaning process (2) P.L.E.:  []
Cleaning process (3) Superset Elimination:  []
SAT
--------------------------------------------
(True, {2: True, -3: True})
```
### Input (UNSAT)
```
formula = [[1, 2, -3, -4], [4, -3, -1], [3], [2, 3, 4], [-3]]
```
### Output
```
Assignment:  {}
Start Formula:  [[1, 2, -3, -4], [4, -3, -1], [3], [2, 3, 4], [-3]]
Cleaning process (1) U.P.:  [[1, 2, -4], [4, -1], []]
Cleaning process (2) P.L.E.:  [[4, -1], []]
Cleaning process (3) Superset Elimination:  [[]]
UNSAT
--------------------------------------------
(False, {})
```
