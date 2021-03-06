from lib import utils
from lib.nodes.node_fac import FacNode
from lib.tokenizer import Tokenizer


class CONST:
    NODE_NAME = 'comp'
    COMP_OP = ['!=', '==', '<', '>', '<=', '>=']
    NOT_EQUAL = COMP_OP[0]
    EQUAL = COMP_OP[1]
    LESS_THAN = COMP_OP[2]
    GREATER_THAN = COMP_OP[3]
    LESS_OR_EQ = COMP_OP[4]
    GREATER_OR_EQ = COMP_OP[5]


class CompNode:
    """
    the comparision node
    <comp> ::= ( <fac> <comp-op> <fac> )
    """

    def __init__(self):
        self.fac_1 = FacNode()
        self.fac_2 = FacNode()
        self.alt = None

    def parse_comp(self, t: Tokenizer):
        """
        parse the comparision node
        :param t: tokenizer
        """
        utils.check_token(t, '(', CONST.NODE_NAME)
        self.fac_1.parse_fac(t)
        if t.current_token in CONST.COMP_OP:
            self.alt = t.current_token
            t.next_token()
        else:
            t.print_error(utils.UTL_STR.P_MISSING_LOGIC_OP.format(CONST.NODE_NAME))
            t.safe_exit()
        self.fac_2.parse_fac(t)
        utils.check_token(t, ')', CONST.NODE_NAME)

    def print_comp(self):
        """
        print the comparision statement
        """
        utils.print_i('(', 0, False)
        self.fac_1.print_fac()
        utils.print_i(' {} '.format(self.alt), 0, False)
        self.fac_2.print_fac()
        utils.print_i(')', 0, False)

    def eval_comp(self):
        """
        evaluate the comparision
        :return: the bool value
        """
        if self.alt == CONST.NOT_EQUAL:
            return self.fac_1.eval_fac() != self.fac_2.eval_fac()
        elif self.alt == CONST.EQUAL:
            return self.fac_1.eval_fac() == self.fac_2.eval_fac()
        elif self.alt == CONST.LESS_THAN:
            return self.fac_1.eval_fac() < self.fac_2.eval_fac()
        elif self.alt == CONST.GREATER_THAN:
            return self.fac_1.eval_fac() > self.fac_2.eval_fac()
        elif self.alt == CONST.LESS_OR_EQ:
            return self.fac_1.eval_fac() <= self.fac_2.eval_fac()
        elif self.alt == CONST.GREATER_OR_EQ:
            return self.fac_1.eval_fac() >= self.fac_2.eval_fac()
