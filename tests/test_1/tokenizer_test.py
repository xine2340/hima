import sys

from lib.tokenizer import Tokenizer

"""
usage: python3 tokenizer_test.py input.core
date: Jan 24, 2017
"""

token_num = {
    'program': 1,
    'begin': 2,
    'end': 3,
    'int': 4,
    'if': 5,
    'then': 6,
    'else': 7,
    'while': 8,
    'loop': 9,
    'read': 10,
    'write': 11,
    'and': 12,
    'or': 13,
    ';': 14,
    ',': 15,
    '=': 16,
    '!': 17,
    '[': 18,
    ']': 19,
    '(': 20,
    ')': 21,
    '+': 22,
    '-': 23,
    '*': 24,
    '!=': 25,
    '==': 26,
    '>=': 27,
    '<=': 28,
    '>': 29,
    '<': 30,
    '###END_OF_FILE###': 33

}
INT_num = 31
ID_num = 32

if len(sys.argv) == 1:
    print("Please enter input file name.")
    exit()

t = Tokenizer(sys.argv[1])

while t.current_token != t.EOF:
    if len(sys.argv) == 3 and sys.argv[2] == 'debug':
        print(t.current_token + ' ', end='')
    if t.current_token in token_num:
        print(token_num[t.current_token])
    elif t.current_token[0].isdigit():
        print(INT_num)
    else:
        print(ID_num)
    t.next_token()
if len(sys.argv) == 3 and sys.argv[2] == 'debug':
    print(t.current_token + ' ', end='')
print(token_num[t.current_token])
