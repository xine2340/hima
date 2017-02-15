def check_token(t, expected, node_name):
    """
    check if current token is expected
    move to next token or print error
    :param t: tokenizer
    :param expected:
    :param node_name:
    """
    token = t.current_token
    if token != expected:
        t.print_error(UTL_STR.P_MISSING_RESV.format(expected, node_name))
        t.safe_exit()
    if t.token_type != t.T_EOF:
        t.next_token()


def check_id(t):
    """
    check if current token is valid identifier
    :param t: tokenizer
    """
    if t.token_type != t.T_ID:
        t.print_error(UTL_STR.P_ID_NOT_FND)
        t.safe_exit()


def print_i(str, indent, new_line=True):
    """
    print string with specified indentation
    :param str: string to print
    :param indent: number of tabs
    :param new_line: ending with new line
    """
    for i in range(0, indent):
        print('  ', end='')
    if new_line:
        print(str)
    else:
        print(str, end='', flush=True)


class UTL_STR:
    P_MISSING_RESV = 'Error: missing reserved word "{}" in {} node/statement.'
    P_MISSING_LOGIC_OP = 'Error: missing logic operator in {} node/statement.'
    P_INVLD_STMT = 'Error: invalid statement.'
    P_INVLD_FAC = 'Error: "{}" is not a valid factor. '
    P_ID_NOT_FND = 'Error: an identifier expected but not found.'
    P_ID_NOT_DCL = 'Error: identifier "{}" is not declared.'
    T_REACH_EOF = 'Reached end of file.'
    T_FILE_NOT_FOUND = 'Error: File not found'
    T_ERROR_LINE = 'Error info:\n\tLine number: {}\n\tNear "{}".'
    T_INVLD_CHAR = 'Error: invalid character.'
    T_NOT_RESV = 'Error: token starts with lower case letter detected; but not a reserved word.'
    T_INT_LET = 'Error: token starts with digit but followed directly by a letter.'
    T_INT_ID_TOO_LONG = 'Error: integer/identifier longer than limit: {}.'
    T_BAD_EOF = 'Error: a token starts with "#" but is not EOF.'
    T_ID_LOW = 'Error: mixing upper and lower cases.'
    T_ID_NUM_LET = 'Error: bad identifier- letter after digits.'
    LEN_LIMIT = 8
    RX_INT_TOO_LONG = '[0-9]{{{},}}'.format(LEN_LIMIT + 1)
    RX_INT_LET = '[0-9]+[A-Za-z]'
    RX_INT = '[0-9]+'
    RX_INT_FULL = '^[0-9]{{1,{}}}$'.format(LEN_LIMIT)
    RX_ID_TOO_LONG = '[A-Z0-9]{{{},}}'.format(LEN_LIMIT + 1)
    RX_ID_NUM_LET = '[A-Z]+[0-9]+[A-Za-z]'
    RX_ID_LOW = '[A-Z]+[0-9]*[a-z]'
    RX_ID = '[A-Z]+[0-9]*'
