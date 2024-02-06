from collections import Counter
import copy

# Global var
branching_default = True

def unit_propagation(formula):
    unit_clauses = [clause[0] for clause in formula if len(clause) == 1]

    clean_formula = []
    for clause in formula:
        for literal in unit_clauses:
            if literal in clause:
                break
            elif -literal in clause:
                clause.remove(-literal)
        else:
            clean_formula.append(clause)

    return clean_formula


def pl_elimination(formula):
    literals = [l for clauses in formula for l in clauses]
    pure_literals = {l : 1 for l in literals if not -l in literals}

    clean_formula = []
    for clause in formula:
        for literal in pure_literals.keys():
            if literal in clause:
                break
        else:
            clean_formula.append(clause)

    return clean_formula


def superset_elimination(formula):
    for clause in formula:
        clause.sort()

    clean_formula = []
    for i1, c1 in enumerate(formula):
        for i2, c2 in enumerate(formula):
           if i1 != i2 and len(c2) <= len(c1) and c2 == c1[:len(c2)]:
                break
        else:
            clean_formula.append(c1)

    return clean_formula


def frequent_literal(formula):
    literals = [l for clause in formula for l in clause]
    count_literals = Counter(literals)
    return max(count_literals, key=count_literals.get)


def dpll(formula, assignment=None):
    if assignment == None:
        assignment = {}

    print('Assignment: ', assignment)

    ### cleaning the input formula
    print('Start Formula: ', formula)

    ## applying unit Propagation
    clean_formula = unit_propagation(copy.deepcopy(formula))
    print('Cleaning process (1) U.P.: ', clean_formula)

    ## applying pure literal elimination
    clean_formula = pl_elimination(clean_formula)
    print('Cleaning process (2) P.L.E.: ', clean_formula)

    ## removing subsume
    clean_formula = superset_elimination(clean_formula)
    print('Cleaning process (3) Superset Elimination: ', clean_formula)

    ### checking empty formula
    if not clean_formula:
        print('SAT', end='\n--------------------------------------------\n')
        return True, assignment

    ### checking for empty any clause
    if any(len(clause) == 0 for clause in clean_formula):

        ## Backtracking
        while True and assignment:
            # removing last assignment
            last_assignment = assignment.popitem()
            # conditions to stop backtracking
            if not assignment or assignment[list(assignment.keys())[-1]] == branching_default or last_assignment[1] == branching_default:
                break

        print('UNSAT', end='\n--------------------------------------------\n')
        return False, assignment

    ### choose literal (most frequent)
    chosen_literal = frequent_literal(clean_formula)
    print('chosen literal: ', chosen_literal, end='\n--------------------------------------------\n')

    ### add the chosen literal to the formula
    new_formula_true ,new_formula_false = list(clean_formula), list(clean_formula)

    ## check if the chosen literal is already in the formula or not
    if not [chosen_literal] in new_formula_true:
        new_formula_true.append([chosen_literal])

    if not [-chosen_literal] in new_formula_false:
        new_formula_false.append([-chosen_literal])

    ### assigning true or false to the chosen literal
    assignment[chosen_literal] = branching_default

    if branching_default: new_formula = new_formula_true
    else: new_formula = new_formula_false
    answer = dpll(new_formula, assignment)

    # check the result
    if answer[0]:
        return (True, answer[1])
    else:
        assignment[chosen_literal] = not branching_default

        if branching_default: new_formula = new_formula_false
        else: new_formula = new_formula_true
        return dpll(new_formula, assignment)
