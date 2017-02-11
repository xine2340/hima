import utils
from node_id import IdNode
from tokenizer import Tokenizer


class CONST:
    SPLIT = ','


class IdListNode:
    """
    the identifier list node
    """

    def __init__(self):
        self.id_list = []

    def parse_id_list(self, t: Tokenizer):
        """
        parse the identifier list
        :param t: tokenizer
        """
        id_node = IdNode.parse_id(t)
        self.id_list.append(id_node)
        while t.current_token == CONST.SPLIT:
            t.next_token()
            id_node = IdNode.parse_id(t)
            self.id_list.append(id_node)

    def print_id_list(self):
        """
        print the id list
        """
        utils.print_i(self.id_list[0].name, 0, False)
        list_len = len(self.id_list)
        for idx in range(1, list_len):
            utils.print_i(CONST.SPLIT + ' ' + self.id_list[idx].name, 0, False)
