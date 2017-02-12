import utils
from nodes.node_id_list import IdListNode
from tokenizer import Tokenizer


class CONST:
    NODE_NAME = 'out'
    OUT = 'write'
    SC = ';'


class OutNode:
    """
    the output node
    <out> ::= write <id-list>;
    """

    def __init__(self):
        self.id_list = IdListNode()

    def parse_out(self, t: Tokenizer):
        """
        parse the output node
        :param t: tokenizer
        """
        utils.check_token(t, CONST.OUT, CONST.NODE_NAME)
        self.id_list.parse_id_list(t)
        utils.check_token(t, CONST.SC, CONST.NODE_NAME)

    def print_out(self, i):
        """
        print the output statement
        :param i: indentation
        """
        utils.print_i(CONST.OUT + ' ', i, False)
        self.id_list.print_id_list()
        print(CONST.SC)

    def exec_out(self):
        """
        execute the output statement
        """
        for id_node in self.id_list.id_list:
            print(id_node.name + ' is ' + str(id_node.value))
