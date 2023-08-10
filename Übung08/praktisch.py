
a = [('B', False)]
b = [('A', True), ('B', True), ('C', False)]
c = [a, b]

# Aufgabe 1
def showClause(clause):
    out = ""
    for i in range(len(clause)):
        if (i > 0):
            out += ' v '
        if (not clause[i][1]):
            out += '~'
        out += clause[i][0]
    return out
    
def showCNF(clauses):
    out = ""
    for i in range(len(clauses)):
        if (i > 0):
            out += ' ^ '
        out += '(' + showClause(clauses[i]) + ')'
    return out

# Aufgabe 2
def alphaLit(lit, alpha):
    return lit[0] in alpha == lit[1]

def alphaClause(clause, alpha):
    if (len(clause) == 0): return False
    return alphaLit(clause[0], alpha) or alphaClause(clause[1:], alpha)

def alphaCNF(clauses, alpha):
    if (len(clauses) == 0): return False
    return alphaClause(clauses[0], alpha) or alphaCNF(clauses[1:], alpha)