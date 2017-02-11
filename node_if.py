from node_cond import CondNode
from node_stmt_seq import StmtSeqNode
from node_cond import CondNode
import utils


class CONST:
    IF = 'if'
    THEN = 'then'
    ELSE = 'else'
    END = 'end'
    SC = ';'
    ALT_IF = 1
    ALT_IF_ELSE = 2


class If_node:
    """
    the if node
    """

    def __init__(self):
        """
        the constructor, creating if node instance
        """
        self.cond = CondNode()
        self.then_seq = StmtSeqNode()
        self.else_seq = False
        self.alt = CONST.ALT_IF
        self.parse_if()

    def parse_if(self, t):
        """
        parse the if node and sub-nodes
        :param t: tokenizer
        """
        utils.check_token(t, CONST.IF)
        self.cond.parse_cond(t)
        utils.check_token(t, CONST.THEN)
        self.then_seq.parse_stmt_seq(t)
        if t.current_token == CONST.ELSE:
            t.next_token()
            self.alt = CONST.ALT_IF_ELSE
            self.else_seq = StmtSeqNode()
            self.else_seq.parse_stmt_seq(t)
        utils.check_token(t, CONST.END)
        utils.check_token(t, CONST.SC)

    def exec_if(self):
        """
        execute the if statement
        """
        if self.cond.eval_cond():
            self.then_seq.exec_stmt_seq()
        elif self.alt == CONST.ALT_IF_ELSE:
            self.else_seq.exec_stmt_seq()

    def print_if(self, i):
        """
        print if statement
        :param i: base indentation
        """
        utils.print_i(CONST.IF, i)
        self.cond.print_cond()
        print(CONST.THEN)
        self.then_seq.print_stmt_seq(i + 1)
        if self.alt == CONST.ALT_IF_ELSE:
            utils.print_i(CONST.ELSE, i)
            self.else_seq.print_stmt_seq(i + 1)
        utils.print_i(CONST.END + CONST.SC, i)
