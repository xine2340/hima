import utils
from nodes.node_comp import CompNode
from tokenizer import Tokenizer


class CONST:
    NODE_NAME = 'cond'
    NOT = '!'
    AND = 'and'
    OR = 'or'
    ALT_CMP = 1
    ALT_NOT = 2
    ALT_AND = 3
    ALT_OR = 4


class CondNode:
    """
    the condition node
    <cond> ::= <comp> | !<cond>
                | [ <cond> and <cond> ]
                | [ <cond> or <cond> ]
    """

    def __init__(self):
        self.alt = None
        self.comp = None
        self.cond_1 = None
        self.cond_2 = None

    def parse_cond(self, t: Tokenizer):
        """
        parse the condition node
        :param t: tokenizer
        """
        if t.current_token == CONST.NOT:
            t.next_token()
            self.alt = CONST.ALT_NOT
            self.cond_1.parse_cond(t)
        elif t.current_token == '[':
            t.next_token()
            self.cond_1.parse_cond(t)
            if t.current_token == CONST.AND:
                t.next_token()
                self.alt = CONST.ALT_AND
            elif t.current_token == CONST.OR:
                t.next_token()
                self.alt = CONST.ALT_OR
            else:
                # todo - error
                # t.print_error()
                t.safe_exit()

            self.cond_2.parse_cond(t)
            utils.check_token(t, ']', CONST.NODE_NAME)
        else:
            self.alt = CONST.ALT_CMP
            self.comp = CompNode()
            self.comp.parse_comp(t)

    def print_cond(self):
        """
        print condition
        """
        if self.alt == CONST.ALT_NOT:
            utils.print_i(CONST.NOT, 0, False)
            self.cond_1.print_cond()
        elif self.alt == CONST.ALT_AND:
            utils.print_i('[', 0, False)
            self.cond_1.print_cond()
            utils.print_i(' {} '.format(CONST.AND), 0, False)
            self.cond_2.print_cond()
            utils.print_i(']', 0, False)
        elif self.alt == CONST.ALT_OR:
            utils.print_i('[', 0, False)
            self.cond_1.print_cond()
            utils.print_i(' {} '.format(CONST.OR), 0, False)
            self.cond_2.print_cond()
            utils.print_i(']', 0, False)
        elif self.alt == CONST.ALT_CMP:
            self.comp.print_comp()

    def eval_cond(self):
        """
        evaluate the condition
        :return: boolean value of the condition
        """
        if self.alt == CONST.ALT_NOT:
            return not self.cond_1.eval_cond()
        elif self.alt == CONST.ALT_AND:
            return self.cond_1.eval_cond() and self.cond_2.eval_cond()
        elif self.alt == CONST.ALT_OR:
            return self.cond_1.eval_cond() or self.cond_2.eval_cond()
        elif self.alt == CONST.ALT_CMP:
            return self.comp.eval_comp()
