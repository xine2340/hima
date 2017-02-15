from lib import utils
from lib.nodes.node_id import IdNode
from lib.tokenizer import Tokenizer


class CONST:
    SPLIT = ','


class IdListNode:
    """
    the identifier list node
    <id-list> ::= <id> | <id>, <id-list>
    """

    def __init__(self):
        self.id_list = []

    def parse_id_list(self, t: Tokenizer, decl=False):
        """
        parse the identifier list
        :param t: tokenizer
        :param decl: is in declaration
        """
        first = True
        while first or t.current_token == CONST.SPLIT:
            if first:
                first = False
            else:
                t.next_token()
            if decl:
                id_node = IdNode.parse_id(t)
            else:
                id_node = IdNode.find_id(t.current_token)
                if id_node is None:
                    t.print_error(utils.UTL_STR.P_ID_NOT_DCL.format(t.current_token))
                    t.safe_exit()
                t.next_token()
            self.id_list.append(id_node)

    def print_id_list(self):
        """
        print the id list
        """
        utils.print_i(self.id_list[0].name, 0, False)
        list_len = len(self.id_list)
        for idx in range(1, list_len):
            utils.print_i(CONST.SPLIT + ' ' + self.id_list[idx].name, 0, False)
