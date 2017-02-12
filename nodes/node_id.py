import utils
from tokenizer import Tokenizer


class IdNode:
    """
    the identifiers node
    containing a static symbol table
    """
    idTable = dict()

    def __init__(self, name):
        self.value = -1
        self.inited = False
        self.name = name

    @staticmethod
    def parse_id(t: Tokenizer):
        """
        parse current id and return the instance
        :param t: tokenizer
        :return: an IdNode instance
        """
        token = t.current_token
        utils.check_id(t)
        t.next_token()
        if token not in IdNode.idTable:
            id_node = IdNode(token)
            IdNode.idTable[token] = id_node
        return IdNode.idTable[token]

    @staticmethod
    def find_id(name):
        if name in IdNode.idTable:
            return IdNode.idTable[name]
        else:
            # todo - error handling
            pass
