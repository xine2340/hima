import utils
from Parser_Nodes.node_exp import ExpNode
from Parser_Nodes.node_id import IdNode


class CONST:
    NODE_NAME = 'assign'
    EQUAL = '='
    SC = ';'


class AssignNode:
    """
    the assign node
    <assign> ::= <id> = <exp>;
    """

    def __init__(self):
        self.id_node = False
        self.exp = ExpNode()

    def parse_assign(self, t):
        """
        parse the assign node
        :param t: tokenizer
        """
        utils.check_id(t)
        self.id_node = IdNode.find_id(t.current_token)
        utils.check_token(t, CONST.EQUAL, CONST.NODE_NAME)
        self.exp.parse_exp(t)
        utils.check_token(t, CONST.SC, CONST.NODE_NAME)

    def print_assign(self, i):
        """
        print the assign node
        :param i: indentation
        """
        utils.print_i(self.id_node.name + '' + CONST.EQUAL + ' ', i, False)
        self.exp.print_exp()
        print(CONST.SC)

    def exec_assign(self):
        """
        execute assign node
        """
        self.id_node.value = self.exp.eval_exp()
