from lib.nodes.node_prog import ProgNode
from lib.tokenizer import Tokenizer

t = Tokenizer("tests/test.core")
p = ProgNode()
p.parse_program(t)
p.print_program()
print()
p.exec_program()



