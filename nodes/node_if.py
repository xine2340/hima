import utils
from Parser_Nodes.node_cond import CondNode
from Parser_Nodes.node_stmt_seq import StmtSeqNode


class CONST:
    NODE_NAME = 'if'
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
    <if> ::= if <cond> then <stmt-seq> end;
            | if <cond> then <stmt-seq> else <stmt-seq> end;
    """

    def __init__(self):
        self.cond = CondNode()
        self.then_seq = StmtSeqNode()
        self.else_seq: StmtSeqNode = False
        self.alt = CONST.ALT_IF

    def parse_if(self, t):
        """
        parse the if node and sub-nodes
        :param t: tokenizer
        """
        utils.check_token(t, CONST.IF, CONST.NODE_NAME)
        self.cond.parse_cond(t)
        utils.check_token(t, CONST.THEN, CONST.NODE_NAME)
        self.then_seq.parse_stmt_seq(t)
        if t.current_token == CONST.ELSE:
            t.next_token()
            self.alt = CONST.ALT_IF_ELSE
            self.else_seq = StmtSeqNode()
            self.else_seq.parse_stmt_seq(t)
        utils.check_token(t, CONST.END, CONST.NODE_NAME)
        utils.check_token(t, CONST.SC, CONST.NODE_NAME)

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
