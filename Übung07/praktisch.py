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
        if ()
