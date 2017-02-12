import utils
from nodes.node_term import TermNode
from tokenizer import Tokenizer


class CONST:
    NODE_NAME = 'exp'
    PLUS = '+'
    MINUS = '-'
    ALT_T = 1
    ALT_TPE = 2
    ALT_TME = 3


class ExpNode:
    """
    the expression node
    <exp> ::= <term> | <term> + <exp> | <term> - <exp>
    """

    def __init__(self):
        self.term = TermNode()
        self.exp: ExpNode = False
        self.alt = CONST.ALT_T

    def parse_exp(self, t: Tokenizer):
        """
        parse the expression node
        :param t: tokenizer
        """
        self.term.parse_term(t)
        if t.current_token == CONST.PLUS:
            t.next_token()
            self.alt = CONST.ALT_TPE
            self.exp = ExpNode()
            self.exp.parse_exp(t)
        elif t.current_token == CONST.MINUS:
            t.next_token()
            self.alt = CONST.ALT_TME
            self.exp = ExpNode()
            self.exp.parse_exp(t)

    def print_exp(self):
        """
        print the expression
        """
        self.term.print_term()
        if self.alt == CONST.ALT_TPE:
            utils.print_i(' ' + CONST.PLUS + ' ', 0, False)
            self.exp.print_exp()
        elif self.alt == CONST.ALT_TME:
            utils.print_i(' ' + CONST.MINUS + ' ', 0, False)
            self.print_exp()

    def eval_exp(self):
        """
        evaluate the expression
        :return: the value of the expression
        """
        value = self.term.eval_term()
        if self.alt == CONST.ALT_TPE:
            value += self.exp.eval_exp()
        elif self.alt == CONST.ALT_TME:
            value -= self.exp.eval_exp()
        return value
