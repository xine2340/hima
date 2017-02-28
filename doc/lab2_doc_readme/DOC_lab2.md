# Documentation for Lab 2

## Design of `node_*` class
The classes for the syntax tree nodes, following the object-oriented
implementation guideline in class. Each node file has a class storing
the constants.

## API
Since there are 17 node classes, we only show the methods in common. For
detailed documentation, please refer to the class file.

#### `parse_*(self, t: Tokenizer)`
>
    parse the corresponding node
    :param t: tokenizer
>

#### `print_*(self, i)`
>
    print the node
    :param i: indentation
>


## Test Plan
All test cases passed; no outstanding bug found.
We used the test cases provided on carmen to test the tokenizer and
parser.
We also tested using the following case
0. missing end
0. missing ;
0. missing )
0. missing then
0. missing ID
0. duplicated reserved words
0. mismatched reserved words
0. nested if/while
0. junk after final end
0. undeclared variable
0. complicated cond/expr
