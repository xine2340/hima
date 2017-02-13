from lib.nodes.node_stmt import StmtNode
from lib.tokenizer import Tokenizer


class CONST:
    STMT_IDF = ['if', 'while', 'read', 'write']


class StmtSeqNode:
    """
    the statement sequence node
    <stmt-seq>::= <stmt> | <stmt> <stmt-seq>
    """

    def __init__(self):
        """
        the constructor, creating statement sequence node instance
        """
        self.stmt_seq = []

    def parse_stmt_seq(self, t: Tokenizer):
        """
        parse the statement sequence
        :param t: tokenizer
        """

        while t.token_type == t.T_ID or t.current_token in CONST.STMT_IDF:
            stmt = StmtNode()
            stmt.parse_stmt(t)
            self.stmt_seq.append(stmt)

    def print_stmt_seq(self, i):
        """
        print the statement sequence
        :param i: indentation
        """
        for stmt in self.stmt_seq:
            stmt.print_stmt(i)

    def exec_stmt_seq(self):
        """
        execute the statement sequence
        """
        for stmt in self.stmt_seq:
            stmt.exec_stmt()
