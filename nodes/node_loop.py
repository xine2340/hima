import utils
from nodes.node_cond import CondNode



class CONST:
    NODE_NAME = 'loop'
    WHILE = 'while'
    LOOP = 'loop'
    END = 'end'
    SC = ';'


class LoopNode:
    """
    the loop node
    <loop> ::= while <cond> loop <stmt-seq> end;
    """

    def __init__(self):
        self.cond = CondNode()
        self.stmt_seq = StmtSeqNode()

    def parse_loop(self, t):
        """
        parse the loop node
        :param t: tokenizer
        """
        utils.check_token(t, CONST.WHILE, CONST.NODE_NAME)
        self.cond.parse_cond(t)
        utils.check_token(t, CONST.LOOP, CONST.NODE_NAME)
        self.stmt_seq.parse_stmt_seq(t)
        utils.check_token(t, CONST.END, CONST.NODE_NAME)
        utils.check_token(t, CONST.SC, CONST.NODE_NAME)

    def print_loop(self, i):
        """
        print the loop statement
        :param i: indentation
        """
        utils.print_i(CONST.WHILE + ' ', i, False)
        self.cond.print_cond()
        utils.print_i(' ' + CONST.LOOP, 0)
        self.stmt_seq.print_stmt_seq(i + 1)
        utils.print_i(CONST.END + CONST.SC, i)

    def exec_loop(self):
        """
        execute the loop statement
        """
        while self.cond.eval_cond():
            self.stmt_seq.exec_stmt_seq()
