from tokenizer import Tokenizer
from node_id_list import IdListNode

t = Tokenizer("test2.core")
idl = IdListNode()
idl.parse_id_list(t)
idl.print_id_list()