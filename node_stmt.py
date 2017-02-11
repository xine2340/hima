import utils
from node_if import If_node
from node_in import In_node
from node_loop import Loop_node
from node_out import Out_node
from tokenizer import Tokenizer
from node_assign import Assign_node


class CONST:
    IF = 'if'
    LOOP = 'loop'
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
    """

    def __init__(self):
        """
        constructor, creating a statement node instance
        """
        self.sub_node = False
        self.alt = False

    def parse_stmt(self, t: Tokenizer):
        """
        parse the statement node
        :param t: tokenizer
        """
        if t.token_type == t.T_ID:
            self.alt = CONST.ALT_ASGN
            self.sub_node = Assign_node()
            self.sub_node.parse_assign(t)
        elif t.current_token == CONST.IF:
            self.alt = CONST.ALT_IF
            self.sub_node = If_node()
            self.sub_node.parse_if(t)
        elif t.current_token == CONST.LOOP:
            self.alt = CONST.ALT_LOOP
            self.sub_node = Loop_node()
            self.sub_node.parse_loop(t)
        elif t.current_token == CONST.IN:
            self.alt = CONST.ALT_IN
            self.sub_node = In_node()
            self.sub_node.parse_in(t)
        elif t.current_token == CONST.OUT:
            self.alt = CONST.ALT_OUT
            self.sub_node = Out_node()
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
