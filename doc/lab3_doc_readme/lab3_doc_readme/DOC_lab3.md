# Documentation for Lab 3

## Design of `node_*` class
We divide the syntax tree into nodes, and each node class handles the
parsing and executing procedures of the corresponding element in the
syntax tree. Based on Lab 2, we added exec and eval methods in each node
class. We also added runtime error checking features.

## API
Since there are 17 node classes, we only show the methods in common. For
detailed API documentation, please refer to the class file.

#### `exec_*(self)`
>
    execute the corresponding node
>

#### `eval_*(self)`
>
    evaluate the corresponding arithmetic/boolean expression, etc
>

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

0. nested if/else
0. nested while loops
0. duplicated declaration
0. numbers larger than max_int
0. use of uninitialized variables