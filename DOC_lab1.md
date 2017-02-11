# Documentation for Lab 1

## Design of `Tokenizer` class
The `Tokenizer` class is basically driven by `next_token()` method.
Next token will be read, and the type of token will be decided once
 `next_token()`. Then the methods named `next_type_name()` will
 the corresponding types of tokens.

## API

#### `__init__(self, source_file):`
>
    The constructor, read the source file
    and initialize the tokenizer instance
    :param source_file: the source file to be tokenized
>

#### `next_token(self):`
>
    get the next token, read next line if current line contains no token,
    terminate and close file when EOF
    :handles errors:
        1. no EOF token
        2. invalid char
>

#### `current_token`
>
    The current token. Following the python's Uniform Access Principle,
    `current_token` is designed as property rather than a method.
>

#### `safe_exit(self):`
>
    close file and exit when error happens
>

#### `print_error(self, error_str):`
>
    print error with the corresponding line number  
    :param error_str: the error string
>

#### `next_reserved(self):`
>
    get a reserved word  
    :handles errors:
        1. not in the reserved list  
        2. bad identifier
    :return: a reserved word in @{reserved}
>

#### `next_symbol(self):`
>
    get a symbol  
    :handles errors:  
    :return: a symbol in @{symbol}
>

#### `next_int(self):`
>    
    get an int  
    :handles errors:  
        1. longer than limit  
        2. followed directly by a letter  
    :return: an int
>    

#### `next_eof(self):`
>    
    get EOF token  
    :return: EOF token
>    

#### `next_id(self):`
>    
    get an identifier  
    :handles errors:  
        1. longer than limit  
        2. letter after letter  
        3. uppercase  
    :return: an identifier
>

## Test Plan
All test cases passed; no outstanding bug found.

0. normal core program file
1. empty file
2. empty file/multiple empty lines with EOF token
3. program without EOF
4. 123Letter
5. ID123LETTER
6. IDentifier
7. prograM
8. program1
9. 12345678
10. 1234567890
11. ABCDEFGH
12. ABCDEFGHI
13. === >== !===
14. (a=b;) (a= b;) (a =b;)