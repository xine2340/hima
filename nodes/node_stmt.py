import utils
from node_in import InNode
from nodes.node_assign import AssignNode
from nodes.node_if import IfNode
from nodes.node_loop import LoopNode
from nodes.node_out import OutNode
from tokenizer import Tokenizer


class CONST:
    IF = 'if'
    LOOP = 'while'
    IN = 'read'
    OUT = 'write'
    ALT_ASGN = 1
    ALT_IF = 2
    ALT_LOOP = 3
    ALT_IN = 4
    ALT_OUT = 5


class StmtNode:
    """
    the statement node
    <stmt> ::= <assign> | <if> | <loop> | <in> | <out>
    """

    def __init__(self):
        self.sub_node = None
        self.alt: int = None

    def parse_stmt(self, t: Tokenizer):
        """
        parse the statement node
        :param t: tokenizer
        """
        if t.token_type == t.T_ID:
            self.alt = CONST.ALT_ASGN
            self.sub_node = AssignNode()
            self.sub_node.parse_assign(t)
        elif t.current_token == CONST.IF:
            self.alt = CONST.ALT_IF
            self.sub_node = IfNode()
            self.sub_node.parse_if(t)
        elif t.current_token == CONST.LOOP:
            self.alt = CONST.ALT_LOOP
            self.sub_node = LoopNode()
            self.sub_node.parse_loop(t)
        elif t.current_token == CONST.IN:
            self.alt = CONST.ALT_IN
            self.sub_node = InNode()
            self.sub_node.parse_in(t)
        elif t.current_token == CONST.OUT:
            self.alt = CONST.ALT_OUT
            self.sub_node = OutNode()
            self.sub_node.parse_out(t)
        else:
            t.print_error(utils.ERR_WARN_STR.P_INVLD_STMT)
            t.safe_exit()

    def print_stmt(self, i):
        """
        print the statement
        :param i: indentation
        """
        if self.alt == CONST.ALT_ASGN:
            self.sub_node.print_assign(i)
        elif self.alt == CONST.ALT_IF:
            self.sub_node.print_if(i)
        elif self.alt == CONST.ALT_LOOP:
            self.sub_node.print_loop(i)
        elif self.alt == CONST.ALT_IN:
            self.sub_node.print_in(i)
        elif self.alt == CONST.ALT_OUT:
            self.sub_node.print_out(i)

    def exec_stmt(self):
        """
        execute the statement
        """
        if self.alt == CONST.ALT_ASGN:
            self.sub_node.exec_assign()
        elif self.alt == CONST.ALT_IF:
            self.sub_node.exec_if()
        elif self.alt == CONST.ALT_LOOP:
            self.sub_node.exec_loop()
        elif self.alt == CONST.ALT_IN:
            self.sub_node.exec_in()
        elif self.alt == CONST.ALT_OUT:
            self.sub_node.exec_out()
