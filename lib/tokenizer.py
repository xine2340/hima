import re

from lib.utils import UTL_STR


class Tokenizer:
    """
    The tokenizer class for CORE language
    date: Jan 24, 2017
    """

    RESERVED = ['program', 'begin', 'end', 'int', 'if', 'then',
                'else', 'while', 'loop', 'read', 'read', 'write',
                'and', 'or']
    SYMBOLS = [';', ',', '!=', '[', ']', '(', ')', '+', '-', '*',
               '!', '==', '<=', '>=', '=', '>', '<']
    EOF = '###END_OF_FILE###'
    T_RESV = 1
    T_SYM = 2
    T_ID = 3
    T_INT = 4
    T_EOF = 5

    def __init__(self, source_file):
        """
        constructor, read the source file
        and initialize the tokenizer instance
        :param source_file: the source file to be tokenized
        """
        try:
            self.source = open(source_file, 'r')
        except FileNotFoundError:
            print(UTL_STR.T_FILE_NOT_FOUND)
            exit()
        self.current_line = ''
        self.line_tokens = []
        self.previous_token = ''
        self.current_token = ''
        self.error_line_num = 0
        self.token_type = 0
        self.next_token()

    def safe_exit(self):
        """
        close file and exit when error happens
        """
        self.source.close()
        exit()

    def print_error(self, error_str):
        """
        print error with the corresponding line number
        :param error_str: the error string
        """
        print(error_str)
        trace_str = self.current_token
        if self.previous_token != '':
            trace_str = self.previous_token + ' ' + trace_str
        if len(self.line_tokens) > 0:
            trace_str = trace_str + ' ' + self.line_tokens[0]
        print(UTL_STR.T_ERROR_LINE.format(self.error_line_num, trace_str.strip()))

    def next_token(self):
        """
        get the next token,
        read next line if current line contains no token,
        terminate and close file when EOF
        :handles errors:
            1. invalid char
        """

        # skip if EOF
        if self.token_type == self.T_EOF:
            print(UTL_STR.T_REACH_EOF)
            return None

        while len(self.line_tokens) == 0 or len(self.line_tokens[0]) == 0:
            # get next line if current line is done
            while len(self.line_tokens) == 0:
                self.current_line = self.source.readline()
                self.error_line_num += 1
                if not self.current_line:
                    self.next_eof()
                    return None
                self.line_tokens = self.current_line.split()

            # pop if head is empty
            if len(self.line_tokens[0]) == 0:
                self.line_tokens.pop(0)

        # get next token
        if self.line_tokens[0][0].islower():
            self.next_reserved()
        elif self.line_tokens[0][0].isupper():
            self.next_id()
        elif self.line_tokens[0][0].isdigit():
            self.next_int()
        elif self.line_tokens[0][0] in self.SYMBOLS:
            self.next_symbol()
        else:
            self.print_error(UTL_STR.T_INVLD_CHAR)
            self.safe_exit()

    def next_reserved(self):
        """
        get a reserved word
        :handles errors:
            1. not in the reserved list
        :return: a reserved word in @{reserved}
        """
        for res in self.RESERVED:
            if self.line_tokens[0].find(res) == 0:
                if len(self.line_tokens[0]) > len(res) and self.line_tokens[0][len(res)].isalnum():
                    continue
                self.previous_token = self.current_token
                self.current_token = res
                self.line_tokens[0] = self.line_tokens[0][len(res):]
                self.token_type = self.T_RESV
                return res

        self.print_error(UTL_STR.T_NOT_RESV)
        self.safe_exit()

    def next_symbol(self):
        """
        get a symbol
        :handles errors:
        :return: a symbol in @{symbol}
        """
        for symbol in self.SYMBOLS:
            if self.line_tokens[0].find(symbol) == 0:
                self.previous_token = self.current_token
                self.current_token = symbol
                self.line_tokens[0] = self.line_tokens[0][len(symbol):]
                self.token_type = self.T_SYM
                return symbol

    def next_int(self):
        """
        get an int
        :handles errors:
            1. longer than limit
            2. followed directly by a letter
        :return: an int string
        """

        if re.match(UTL_STR.RX_INT_TOO_LONG, self.line_tokens[0]) is not None:
            self.print_error(UTL_STR.T_INT_ID_TOO_LONG.format(UTL_STR.LEN_LIMIT))
            self.safe_exit()
        elif re.match(UTL_STR.RX_INT_LET, self.line_tokens[0]) is not None:
            self.print_error(UTL_STR.T_INT_LET)
            self.safe_exit()
        else:
            self.previous_token = self.current_token
            self.current_token = re.match(UTL_STR.RX_INT, self.line_tokens[0]).group(0)
            self.line_tokens[0] = self.line_tokens[0][len(self.current_token):]
            self.token_type = self.T_INT
            return self.current_token

    def next_eof(self):
        """
        get EOF token
        :return: EOF token
        """
        self.previous_token = self.current_token
        self.current_token = self.EOF
        self.source.close()
        self.token_type = self.T_EOF

    def next_id(self):
        """
        get an identifier
        :handles errors:
            1. longer than limit
            2. letter after number
            3. lowercase
        :return: an identifier
        """

        if re.match(UTL_STR.RX_ID_TOO_LONG, self.line_tokens[0]) is not None:
            self.print_error(UTL_STR.T_INT_ID_TOO_LONG.format(UTL_STR.LEN_LIMIT))
            self.safe_exit()
        elif re.match(UTL_STR.RX_ID_NUM_LET, self.line_tokens[0]) is not None:
            self.print_error(UTL_STR.T_ID_NUM_LET)
            self.safe_exit()
        elif re.match(UTL_STR.RX_ID_LOW, self.line_tokens[0]) is not None:
            self.print_error(UTL_STR.T_ID_LOW)
            self.safe_exit()
        else:
            self.previous_token = self.current_token
            self.current_token = re.match(UTL_STR.RX_ID, self.line_tokens[0]).group(0)
            self.line_tokens[0] = self.line_tokens[0][len(self.current_token):]
            self.token_type = self.T_ID
            return self.current_token
