import utils
from Parser_Nodes.node_id_list import IdListNode


class CONST:
    NODE_NAME = 'declaration'
    INT = 'int'
    SC = ';'


class DeclNode:
    """
    the declaration node
    <decl-seq>::= <decl> | <decl> <decl-seq>
    """

    def __init__(self):
        self.id_list = IdListNode()

    def parse_decl(self, t):
        """
        parse the declaration node
        :param t: tokenizer
        """
        utils.check_token(t, CONST.INT, CONST.NODE_NAME)
        self.id_list.parse_id_list(t)
        utils.check_token(t, CONST.SC, CONST.NODE_NAME)

    def print_decl(self, i):
        """
        print the declaration node
        :param i: indentation
        """
        utils.print_i(CONST.INT + ' ', i, False)
        self.id_list.print_id_list()
        print(CONST.SC)
