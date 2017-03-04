from lib import utils
from lib.tokenizer import Tokenizer


class IdNode:
    """
    the identifiers node, initialized to 0
    the class contains a static symbol table
    """
    idTable = dict()

    def __init__(self, name):
        self.value = None
        self.name = name

    @staticmethod
    def parse_id(t: Tokenizer):
        """
        parse current id (in decl-seq) and return the instance
        :param t: tokenizer
        :return: an IdNode instance
        """
        token = t.current_token
        utils.check_id(t)
        t.next_token()
        if token not in IdNode.idTable:
            id_node = IdNode(token)
            IdNode.idTable[token] = id_node
        else:
            t.print_error(utils.UTL_STR.P_ID_DUP_DCL.format(token))
            t.safe_exit()
        return IdNode.idTable[token]

    @staticmethod
    def find_id(name):
        """
        find the id in the symbol table
        :param name: id name
        :return: id or none
        """
        if name in IdNode.idTable:
            return IdNode.idTable[name]
        else:
            return None

    def eval_id(self):
        """
        :return: value of the id
        """
        if self.value is None:
            print(utils.UTL_STR.R_ID_NOT_INIT.format(self.name))
            exit()
        else:
            return self.value
