# Niht-Rekursiver Parser in Python

T = ('id', '(', ')', ':=', '+', '-', '*', '/')

N = (0,1,2,3,4,5,6,7,8,9)

parse_table = ({'id': (1) ,  '$$': (1) },
               {'id': (2, 1), '$$': ()},
               {'id': ('id', ':=', 3)},
               {'id': (5, 4), '(':(5, 4)},
               {'id': (), ')': (), '+': (8, 5, 4), '-':(8, 5, 4), '$$': ()},
               {'id': (7, 6), '(': (7, 6)},
               {'id': (), ')': (), '+': (), '-': (), '*': (9, 7, 6), '/': (9, 7, 6), '$$': ()},
               {'id': ('id'), '(': ('(', 3, ')')},
               {'+': '+', '-': '-'},
               {'*': '*', '/': '/'})


def input_prep(input):
    input_list = []
    i = 0
    while i < len(input):
        if (input[i] == 'i'):
            if (i+1 < len(input)):
                if (input[i+1] == 'd'):
                    input_list.append('id')
                    i += 1
                else:
                    error()
            else:
                error()
        elif (input[i] == ':'):
            if(i+1 < len(input)):
                if (input[i+1] == '='):
                    input_list.append(':=')
                    i += 1
                else:
                    error()
            else:
                error()
        elif (input[i] in T):
            input_list.append(input[i])
        else:
            error()
        i += 1
    input_list.append('$$')
    return input_list

def error():
    print('ERROR')
    exit()


def parse(input):
    stack = [0]
    while (len(stack) > 0):
        if (stack[0] in N):
            if (input[0] not in parse_table[stack[0]]): error()
            val = parse_table[stack.pop(0)][input[0]]
            if (isinstance(val, tuple)):
                for v in reversed(val):
                    stack.insert(0,v)
            else:
                stack.insert(0, val)
        elif (stack[0] in T):
            if(len(input) == 0): error()
            if (stack[0] == input[0]):
                input.pop(0)
                stack.pop(0)
            else:
                error()
        else:
            error()
    if (len(input) > 1): error()
    print('Successful')
    return stack


inp = input()
print(parse(input_prep(inp)))
