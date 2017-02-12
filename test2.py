from nodes.node_prog import ProgNode
from tokenizer import Tokenizer

t = Tokenizer("test.core")
p = ProgNode()
p.parse_program(t)
p.print_program()
print()
p.exec_program()



