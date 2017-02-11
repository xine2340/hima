from enum import Enum


def check_token(t, expected):
    """
    check if current token is expected
    move to next token or print error
    :param t: tokenizer
    :param expected:
    """
    token = t.current_token
    if token != expected:
        t.print_error(ERR_WARN_STR.P_MISSING_RESV.format(expected))
        t.safe_exit()
    if t.token_type != t.T_EOF:
        t.next_token()


def check_id(t):
    """
    check if current token is valid identifier
    :param t: tokenizer
    """
    if t.token_type != t.T_ID:
        t.print_error(ERR_WARN_STR.P_ID_NOT_FND)
        t.safe_exit()


def print_i(str, indent, new_line=True):
    """
    print string with specified indentation
    :param str: string to print
    :param indent: number of tabs
    :param new_line: ending with new line
    """
    for i in range(0, indent):
        print('\t', end='')
    if new_line:
        print(str)
    else:
        print(str, end='', flush=True)


class ERR_WARN_STR:
    P_MISSING_RESV = 'Error: missing reserved word "{}".'
    P_INVLD_STMT = 'Error: invalid statement.'
    P_ID_NOT_FND = 'Error: an identifier expected but not found.'
    T_REACH_EOF = 'Reached end of file.'
    T_FILE_NOT_FOUND = 'Error: File not found'
    T_ERROR_LINE = 'Error info:\n\tLine number: {}\n\tNear "{}".'
    T_MISSING_EOF = 'Error: invalid end of file; missing EOF token.'
    T_INVLD_CHAR = 'Error: invalid character.'
    T_NOT_RESV = 'Error: token starts with lower case letter detected; but not a reserved word.'
    T_INT_LET = 'Error: token starts with digit but followed directly by a letter.'
    T_INT_ID_TOO_LONG = 'Error: integer/identifier longer than limit: {}.'
    T_BAD_EOF = 'Error: a token starts with "#" but is not EOF.'
    T_ID_LOW = 'Error: mixing upper and lower cases.'
    T_ID_NUM_LET = 'Error: bad identifier- letter after digits.'


class CNST(Enum):
    pass
