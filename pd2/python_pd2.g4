grammar python_pd2;

//root catch
program: statement+ ; 

//defines statements with assignment or control flow
statement
    : assignment                     // assignment statements
    | if_block                       // if/elif/else blocks
    ;

//checks for variables with different assignments to expressions.
assignment
    : VARIABLE ASSIGN expression      # catches variable = expression
    | VARIABLE ADD_ASSIGN expression  # catches variable += expression
    | VARIABLE SUB_ASSIGN expression  # catches variable -= expression
    | VARIABLE MUL_ASSIGN expression  # catches variable *= expression
    | VARIABLE DIV_ASSIGN expression  # catches variable /= expression 
    ;

//handles if/elif/else blocks
if_block
    : IF condition COLON block (ELIF condition COLON block)* (ELSE COLON block)?
    ;

//handles blocks (indented statements)
block: statement+ ;

//checks for different types of conditions for if/elif
condition
    : expression comparison expression            # comparison operators
    | NOT condition                               # not condition
    | condition AND condition                     # and condition
    | condition OR condition                      # or condition
    ;

//expression tree; allows for any number of expressions to be nested by recursion.
//
expression
    : expression ADD expression       # expression + expression
    : expression SUB expression       # expression - expression
    | expression MUL expression       # expression * expression
    | expression DIV expression       # expression / expression
    | expression MOD expression       # expression mod expression
    | '(' expression ')'              # (parantheses)
    | list                            # list
    | STRING                          # string
    | NUMBER                          # number
    | VARIABLE                        # variable
    ;

//specifies lists.
list: '[' expression (',' expression)* ']' ;

//handles comparison operators
comparison
    : '<'       // catches less than
    | '<='      // catches less than or equal
    | '>'       // catches greater than
    | '>='      // catches greater than or equal
    | '=='      // catches equal
    | '!='      // catches not equal
    ;

//simply definitions for non-terms used earlier.
ASSIGN     : '=' ;
ADD_ASSIGN : '+=' ;
SUB_ASSIGN : '-=' ;
MUL_ASSIGN : '*=' ;
DIV_ASSIGN : '/=' ;

//simply definitions for non-terms used earlier.
ADD        : '+' ;
SUB        : '-' ;
MUL        : '*' ;
DIV        : '/' ;
MOD        : '%' ;

//handles logical operators
AND        : 'and' ;
OR         : 'or' ;
NOT        : 'not' ;

//keywords for if/elif/else
IF         : 'if' ;
ELIF       : 'elif' ;
ELSE       : 'else' ;
COLON      : ':' ;

//tokens for variables and numbers.
//variables allow for a-z or A-Z, but no numbers, then any number of a-z, A-Z, 0-9 or _.
//numbers allow for 1 or more 0-9, then, a . or 1 or more 0-9 for dec, with ? specifying optionality.
VARIABLE   : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER     : [0-9]+ ('.' [0-9]+)? ;

//catches both single quote and double quote strings
STRING     : ('"' .*? '"') | ('\'' .*? '\'');

//catches comma for lists
COMMA      : ',' ;

//skips python whitespace
WS : [ \t\r\n]+ -> skip ;
