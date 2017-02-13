from lib.nodes.node_id import IdNode

import lib.nodes.node_exp
from lib import utils
from lib.tokenizer import Tokenizer


class CONST:
    NODE_NAME = 'fac'
    ALT_INT = 1
    ALT_ID = 2
    ALT_EXP = 3


class FacNode:
    """
    the factor node
    <fac> ::= <int> | <id> | ( <exp> )
    """

    def __init__(self):
        self.int_val = None
        self.id_node = None
        self.exp = None
        self.alt = None

    def parse_fac(self, t: Tokenizer):
        """
        parse the factor node
        :param t: tokenizer
        """
        if t.token_type == t.T_INT:
            self.alt = CONST.ALT_INT
            self.int_val = int(t.current_token)
            t.next_token()
        elif t.token_type == t.T_ID:
            self.alt = CONST.ALT_ID
            self.id_node = IdNode.find_id(t.current_token)
            t.next_token()
        elif t.current_token == '(':
            t.next_token()
            self.exp = lib.nodes.node_exp.ExpNode()
            self.exp.parse_exp(t)
            utils.check_token(t, ')', CONST.NODE_NAME)
        else:
            t.print_error(utils.ERR_WARN_STR.P_INVLD_FAC.format(t.current_token))
            t.safe_exit()

    def print_fac(self):
        """
        print the factor
        """
        if self.alt == CONST.ALT_INT:
            utils.print_i(self.int_val, 0, False)
        elif self.alt == CONST.ALT_ID:
            utils.print_i(self.id_node.name, 0, False)
        elif self.alt == CONST.ALT_EXP:
            utils.print_i('(', 0, False)
            self.exp.print_exp()
            utils.print_i(')', 0, False)

    def eval_fac(self):
        """
        evaluate the factor
        :return: value of the factor
        """
        if self.alt == CONST.ALT_INT:
            return self.int_val
        elif self.alt == CONST.ALT_ID:
            return self.id_node.value
        elif self.alt == CONST.ALT_EXP:
            return self.exp.eval_exp()
