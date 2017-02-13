from lib import utils
from lib.nodes.node_fac import FacNode


class CONST:
    NODE_NAME = 'term'
    TIMES = '*'
    ALT_FAC = 1
    ALT_FAC_TERM = 2


class TermNode:
    """
    the term node:
    <term> ::= <fac> | <fac> * <term>
    """

    def __init__(self):
        self.fac = FacNode()
        self.term = None
        self.alt = None

    def parse_term(self, t):
        """
        parse the term node
        :param t: tokenizer
        """
        self.alt = CONST.ALT_FAC
        self.fac.parse_fac(t)
        if t.current_token == CONST.TIMES:
            self.alt = CONST.ALT_FAC_TERM
            t.next_token()
            self.term = TermNode()
            self.term.parse_term(t)

    def print_term(self):
        """
        print the term
        """
        if self.alt == CONST.ALT_FAC:
            self.fac.print_fac()
        elif self.alt == CONST.ALT_FAC_TERM:
            self.fac.print_fac()
            utils.print_i(' {} '.format(CONST.TIMES), 0, False)
            self.term.print_term()

    def eval_term(self):
        """
        evaluate the term
        :return: the value of the term
        """
        if self.alt == CONST.ALT_FAC:
            return self.fac.eval_fac()
        elif self.alt == CONST.ALT_FAC_TERM:
            return self.fac.eval_fac() * self.term.eval_term()
