from lib import utils
from lib.nodes.node_id_list import IdListNode


class CONST:
    NODE_NAME = 'declaration'
    TYPES = ['int']
    INT = TYPES[0]
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
        if t.current_token in CONST.TYPES:
            t.next_token()
        self.id_list.parse_id_list(t, True)
        utils.check_token(t, CONST.SC, CONST.NODE_NAME)

    def print_decl(self, i):
        """
        print the declaration node
        :param i: indentation
        """
        utils.print_i(CONST.INT + ' ', i, False)
        self.id_list.print_id_list()
        print(CONST.SC)
