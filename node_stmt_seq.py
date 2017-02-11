from node_stmt import StmtNode
from tokenizer import Tokenizer


class CONST:
    STMT_IDF = ['if', 'loop', 'read', 'write']


class StmtSeqNode:
    """
    the statement sequence node class
    """

    def __init__(self):
        """
        the constructor, creating statement sequence node instance
        """
        self.stmt_list = []

    def parse_stmt_seq(self, t: Tokenizer):
        """
        parse the statement sequence
        :param t: tokenizer
        """
        # TODO - handle empty stmt seq
        while t.token_type == t.T_ID or t.token_type in CONST.STMT_IDF:
            stmt = StmtNode()
            stmt.parse_stmt(t)
            self.stmt_list.append(stmt)

    def print_stmt_seq(self, i):
        """
        print the statement sequence
        :param i: indentation
        """
        for stmt in self.stmt_list:
            stmt.print_stmt(i)

    def exec_stmt_seq(self):
        """
        execute the statement sequence
        """
        for stmt in self.stmt_list:
            stmt.exec_stmt()
