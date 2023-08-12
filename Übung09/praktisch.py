import sys


# Aufgabe 1
def main():
    x = 0
    if (len(sys.argv) > 1):
        x = int(sys.argv[1])
    if (len(sys.argv) == 2):
        print(int(x))
        print(bin(x)[2:])
    elif (len(sys.argv) == 4):
        a = int(sys.argv[2])
        b = int(sys.argv[3])
        first = min(a, b)
        last = max(a, b)-1
        first = first % (len(bin(x)[2:])+1)
        last = last % (len(bin(x)[2:])+1)

        biny = '0b0'
        for i in range(min(first, last), max(first, last)):
            biny += bin(x)[2:][i]
        print(biny)
        print(int(biny, 2))
    else:
        raise(IndexError('Falsche Anzahl an Argumenten'))

# Aufgabe 2


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


def check_for_res(comp, tocmp):
    res = []
    for lit1 in comp:
        lit2 =(lit1[0], not lit1[1])
        if lit2 in tocmp:
            res1 = comp + tocmp
            for lit in res1:
                while (res1.count(lit) > 1):
                    res1.remove(lit)
            res1.remove(lit1)
            res1.remove(lit2)
            res1.sort()
            res += [res1]
    for i in res:
        while (res.count(i) > 1):
            res.remove(i)
    return res

def build_res(clauses):
    res = clauses.copy()
    for clause1 in clauses:
            for clause2 in clauses:
                if (clause1 is clause2):
                    continue
                res1 = check_for_res(clause1, clause2)
                if (not res1):
                    continue
                res += res1
                for i in res:
                    while (res.count(i) > 1):
                        res.remove(i)
    return res



a = [('X', True), ('Y', False)]
b = [('X', False), ('Y', False), ('Z', False)]
c = [('X', False), ('Z', True)]
d = [('X', True), ('Y', True), ('Z', True)]
e = [('Y', True), ('Z', False)]
f = [a, b, c, d, e]

def erfüllbar(clauses):
    res0 = clauses.copy()
    res1 = build_res(res0)
    while(res0 != res1 and [] not in res1):
        print(showCNF(res0))
        res0 = res1.copy()
        res1 = build_res(res1)
    print(showCNF(res1))
    if ([] in res1):
        print('Formel nicht erfüllbar')
    else:
        print('Formel erfüllbar')

er = [[('X', True), ('X', False)], [('Y', False), ('Y',True)]]

erfüllbar(f)


