grammar python_pd1;

//root catch
program: statement+ ; 

//defines statements with assignment
statement: assignment ;

// checks for variables with different assignments to expressions.
assignment
    : VARIABLE ASSIGN expression      # catches variable = expression
    | VARIABLE ADD_ASSIGN expression  # catches variable += expression
    | VARIABLE SUB_ASSIGN expression  # catches variable -= expression
    | VARIABLE MUL_ASSIGN expression  # catches variable *= expression
    | VARIABLE DIV_ASSIGN expression  # catches variable /= expression 
    ;

//expression tree; allows for any number of expressions to be nested by recursion.
//
expression
    : expression ADD expression       # expression + expression
    | expression SUB expression       # expression - expression
    | expression MUL expression       # expression * expression
    | expression DIV expression       # expression / expression
    | expression MOD expression       # expression mod expression
    | '(' expression ')'              # (parantheses)
    | list                            # list
    | STRING                          # string
    | NUMBER                          # number
    | VARIABLE                        # variable
    ;

// specifies lists.
list: '[' expression (',' expression)* ']' ;

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
