import utils
from nodes.node_decl_seq import DeclSeqNode
from nodes.node_stmt_seq import StmtSeqNode


class CONST:
    NODE_NAME = 'program'
    PROG = 'program'
    BEGIN = 'begin'
    END = 'end'


class ProgNode:
    """
    the program node
    <prog> ::= program <decl-seq> begin <stmt-seq> end
    """

    def __init__(self):
        self.decl_seq = DeclSeqNode()
        self.stmt_seq = StmtSeqNode()

    def parse_program(self, t):
        """
        parse program and sub-nodes
        :param t: tokenizer
        """
        utils.check_token(t, CONST.PROG, CONST.NODE_NAME)
        self.decl_seq.parse_decl_seq(t)
        utils.check_token(t, CONST.BEGIN, CONST.NODE_NAME)
        self.stmt_seq.parse_stmt_seq(t)
        utils.check_token(t, CONST.END, CONST.NODE_NAME)
        # utils.check_token(t, t.EOF, CONST.END)

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
        # self.decl_seq.exec_decl_seq()
        self.stmt_seq.exec_stmt_seq()
