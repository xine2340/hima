from node_decl_seq import DeclSeqNode
from node_stmt_seq import StmtSeqNode
import utils
from tokenizer import Tokenizer


class CONST:
    PROG = 'program'
    BEGIN = 'begin'
    END = 'end'


class ProgNode:
    """
    the program node
    """

    def __init__(self):
        self.decl_seq = DeclSeqNode()
        self.stmt_seq = StmtSeqNode()

    def parse_program(self, t: Tokenizer):
        """
        parse program and sub-nodes
        """
        utils.check_token(t, CONST.PROG)
        self.decl_seq.parse_decl_seq_node(t)
        utils.check_token(t, CONST.BEGIN)
        self.stmt_seq.parse_stmt_seq(t)
        utils.check_token(t, CONST.END)
        utils.check_token(t, t.EOF)

    def print_program(self):
        """
        print the program
        """
        utils.print_i(CONST.PROG, 0)
        self.decl_seq.print_decl_seq(1)
        utils.print_i(CONST.BEGIN, 1)
        self.stmt_seq.print_stmt_seq(2)
        utils.print_i(CONST.END, 1)

    def exec_program(self):
        """
        execute the program
        """
        self.decl_seq.exec_decl_seq()
        self.stmt_seq.exec_stmt_seq()
