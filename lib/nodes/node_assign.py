from lib.nodes.node_id import IdNode

from lib import utils
from lib.nodes.node_exp import ExpNode
from lib.tokenizer import Tokenizer


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
        self.id_node = None
        self.exp = ExpNode()

    def parse_assign(self, t: Tokenizer):
        """
        parse the assign node
        :param t: tokenizer
        """
        utils.check_id(t)
        self.id_node = IdNode.find_id(t.current_token)
        if self.id_node is None:
            t.print_error(utils.UTL_STR.P_ID_NOT_DCL.format(t.current_token))
            t.safe_exit()
        t.next_token()
        utils.check_token(t, CONST.EQUAL, CONST.NODE_NAME)
        self.exp.parse_exp(t)
        utils.check_token(t, CONST.SC, CONST.NODE_NAME)

    def print_assign(self, i):
        """
        print the assign node
        :param i: indentation
        """
        utils.print_i(self.id_node.name + ' ' + CONST.EQUAL + ' ', i, False)
        self.exp.print_exp()
        print(CONST.SC)

    def exec_assign(self):
        """
        execute assign node
        """
        self.id_node.value = self.exp.eval_exp()
