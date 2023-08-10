
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
    return (lit[0] in alpha and lit[1]) or (not lit[0] in alpha and not lit[1])

def alphaClause(clause, alpha):
    if (len(clause) == 0): return False
    return alphaLit(clause[0], alpha) or alphaClause(clause[1:], alpha)

def alphaCNF(clauses, alpha):
    if (len(clauses) == 0): return True
    return alphaClause(clauses[0], alpha) and alphaCNF(clauses[1:], alpha)

# Aufgabe 3
alphabet = ['A', 'B']

print("Unerfüllende Belegung: %s" %(showCNF(c)))
print(alphaCNF(c, alphabet))

a = [('B', True)]
c = [a,b]
print("Erfüllende Belegung: %s" %(showCNF(c)))
print(alphaCNF(c, alphabet))