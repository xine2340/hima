import sys

from lib.nodes.node_prog import ProgNode
from lib.tokenizer import Tokenizer

"""
usage: python3 lab2main.py input.core
date: Feb 10, 2017
"""

if len(sys.argv) == 1:
    print("Please enter input file name.")
    exit()

t = Tokenizer(sys.argv[1])

p = ProgNode()
p.parse_program(t)
p.print_program()
