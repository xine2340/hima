import utils
from Parser_Nodes.node_fac import FacNode


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
        self.alt = False

    def parse_comp(self, t):
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
            # todo - error
            pass
        self.fac_2.parse_fac(t)

    def print_comp(self):
        """
        print the comparision statement
        """
        utils.print_i('(', 0, False)
        self.fac_1.print_fac()
        utils.print_i(' {} '.format(self.alt), 0, False)
        self.fac_2.print_fac()

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
