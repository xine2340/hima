import re

from lib.nodes.node_id_list import IdListNode
from lib import utils


class CONST:
    NODE_NAME = 'input'
    IN = 'read'
    SC = ';'
    PROMPT = '{} =? '
    INV_VAL = 'Enter a valid value for {{}} (Non-negative integer with length less than {}): '.format(
        utils.UTL_STR.LEN_LIMIT)


class InNode:
    """
    the input node
    <in> ::= read <id-list>;
    """
    pass

    def __init__(self):
        self.id_list = IdListNode()

    def parse_in(self, t):
        """
        parse the input node
        :param t: tokenizer
        """
        utils.check_token(t, CONST.IN, CONST.NODE_NAME)
        utils.check_id(t)
        self.id_list.parse_id_list(t)
        utils.check_token(t, CONST.SC, CONST.NODE_NAME)

    def print_in(self, i):
        """
        print the input statement
        :param i: indentation
        """
        utils.print_i(CONST.IN + ' ', i, False)
        self.id_list.print_id_list()
        print(CONST.SC)

    def exec_in(self):
        """
        execute the input statement
        """
        for i in self.id_list.id_list:
            v = input(CONST.PROMPT.format(i.name))
            while re.match(utils.UTL_STR.RX_INT_FULL, v) is None:
                v = input(CONST.INV_VAL.format(i.name))
            i.value = int(re.match(utils.UTL_STR.RX_INT_FULL, v).group(0))
