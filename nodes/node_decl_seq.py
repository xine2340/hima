import nodes.node_decl
from nodes.node_decl import DeclNode
from tokenizer import Tokenizer


class DeclSeqNode:
    """
    the deceleration sequence node
    <decl-seq>::= <decl> | <decl> <decl-seq>
    """

    def __init__(self):
        self.decl_seq = []

    def parse_decl_seq(self, t: Tokenizer):
        """
        parse the declaration sequence node
        :param t: tokenizer
        """
        while t.current_token in nodes.node_decl.CONST.TYPES:
            decl = DeclNode()
            decl.parse_decl(t)
            self.decl_seq.append(decl)

    def print_decl_seq(self, i):
        """
        print the declaration sequence
        :param i: indentation
        """
        for decl in self.decl_seq:
            decl.print_decl(i)
