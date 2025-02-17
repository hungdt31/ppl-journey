// 2211322
grammar MiniGo;

@lexer::header {
# 2211322
from lexererr import *
}

@lexer::members {
def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.preType = None

def emit(self):
    tk = self.type
    self.preType = tk;
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language = Python3;
}

// ! ---------------- LEXER ----------------------- */

//TODO Keywords 3.3.2 pdf
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';
//, self.BINARY_LIT, self.OCT_LIT, self.HEXA_LIT, 
SEMICOLON: ';' | '\r'? '\n' {
    if self.preType in {
        self.CP, self.CCB, self.CSB, 
        self.INT_LIT, self.FLOAT_LIT, self.STRING_LIT, 
        self.TRUE, self.FALSE, self.ID, self.BREAK, 
        self.CONTINUE, self.RETURN, self.NIL
    }:
        self.text = ';'
    else:
        self.skip()
};

//TODO Operators 3.3.3 pdf
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '==';
NOT_EQUAL: '!=';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';
// Logical
LOGICAL_OR  : '||';
LOGICAL_AND : '&&';
LOGICAL_NOT : '!';
SHORT_DECL: ':=';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
ASSIGN: '=';
DOT: '.';

//TODO Separators 3.3.4 pdf
OP: '('; // "open parenthesis"
CP: ')'; // "close parenthesis"
OSB: '['; // "open square bracket"
CSB: ']'; // "close square bracket"
OCB: '{'; // "open curly bracket"
CCB: '}'; // "close curly bracket"
COMMA: ',';

//TODO Identifiers 3.3.1 pdf
ID: [a-zA-Z_][a-zA-Z0-9_]*; // Ex: x, userName, _tempVar, count123

//TODO Literal 3.3.5 pdf
INT_LIT: DECIMAL_LIT | BINARY_LIT | OCTAL_LIT | HEX_LIT;
fragment DECIMAL_LIT: '0' | ([1-9] [0-9]*);
fragment HEX_LIT: '0' [xX] [0-9a-fA-F]+;
fragment BINARY_LIT: '0' [bB] [01]+;
fragment OCTAL_LIT: '0' [oO] [0-7]+;

// Floating-Point Literals
FLOAT_LIT: DECIMALS '.' [0-9]* EXPONENT?;
fragment DECIMALS: [0-9]+;
fragment EXPONENT: [eE] [+\-]? [0-9]+;

//TODO skip 3.1 and 3.2 pdf
WS: [ \t\r\f]+ -> skip; // skip tabs 
COMMENT : '/*' (COMMENT|.)*? '*/' -> skip;
// TERMINATOR: [\r\n]+ -> skip; // skip newlines, spaces
LINE_COMMENT: '//' ~[\r\n]* -> skip;

//TODO ERROR pdf BTL1 + lexererr.py
// { self.text = self.text[1:-1] }
STRING_LIT: '"' STR_CHAR* '"';                 
fragment ESCAPED_VALUE: '\\' [ntr"\\];
fragment STR_CHAR: ~[\r\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [rnt"\\];
fragment ESC_ILLEGAL: [\r] | '\\' ~[rnt'\\];

//! ---------------- END OF LEXER ----------------------- */

//! ---------------- PARSER ----------------------- */
program: list_decl EOF;
list_decl: decl SEMICOLON list_decl | decl SEMICOLON;
decl: const_decl | var_decl | func_decl | struct_decl | interface_decl | method_decl;
const_decl: CONST ID ASSIGN expression;
var_decl: VAR ID (param_type | (ASSIGN expression) | (param_type ASSIGN expression));
primitive_type: INT | FLOAT | STRING | BOOLEAN;
boolean_literal: TRUE | FALSE;
//TODO Literal 6.6 pdf
primitive_literal: NIL | INT_LIT | FLOAT_LIT | boolean_literal | STRING_LIT;
literal: primitive_literal | struct_literal | array_literal;

//TODO Array Type
array_bracket: OSB (INT_LIT | ID) CSB array_bracket| OSB (INT_LIT | ID) CSB;
type_return: array_bracket? (ID | primitive_type);
array_literal: array_bracket (ID | primitive_type) OCB array_lit_elements CCB;
array_lit_elements: array_lit_element COMMA array_lit_element | array_lit_element;
array_lit_element: OCB array_lit_element CCB | array_lit_element COMMA array_lit_element_1 | array_lit_element_1;
array_lit_element_1: primitive_literal | struct_literal | ID;

struct_literal: ID OCB struct_element? CCB;
struct_element: ID ':' expression COMMA struct_element | ID ':' expression;

// 4.7 Interface type
interface_decl: TYPE ID INTERFACE OCB method_interface_decl CCB;
method_interface_decl: method_field SEMICOLON method_interface_decl | method_field SEMICOLON;
method_field: ID OP method_params? CP param_type?;
method_params: ID param_type? COMMA method_params | ID param_type;
// 4.6 Struct type
struct_decl: TYPE ID STRUCT OCB struct_decl_elements CCB;
struct_decl_element: ID type_return;
struct_decl_elements: struct_decl_element SEMICOLON struct_decl_elements | struct_decl_element SEMICOLON;

// TODO 5.2 Expressions 6 pdf
list_expression: expression COMMA list_expression | expression;
expression: expression LOGICAL_OR expression1 | expression1;
expression1: expression1 LOGICAL_AND expression2 | expression2;
expression2: expression2 (EQUAL | NOT_EQUAL | LT | GT | LE | GE) expression3 | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: (LOGICAL_NOT | SUB) expression5 | expression6;
expression6: expression6 DOT expression7_1 | expression6 OSB expression CSB | expression7_2;
expression7_1: ID | func_call;
expression7_2: ID | literal | func_call | OP expression CP;
func_call: ID OP list_expression? CP;

// TODO: 5.3 Functions and Methods
params: ID param_type COMMA params | ID param_type;
param_type: param_type OSB INT_LIT CSB| OSB INT_LIT CSB param_type| param_type_1;
param_type_1: primitive_type | ID;
func_decl: FUNC ID OP method_params? CP type_return? OCB list_statement CCB;
method_decl: FUNC OP ID ID CP ID OP method_params? CP expression? (primitive_type | ID)? OCB list_statement CCB;

//TODO Statement 5 and 4 pdf
list_statement: statement SEMICOLON list_statement | statement SEMICOLON;
// TODO: 7 Statements
declared_statement: var_decl | const_decl;
statement: 
    declared_statement
    | assign_statement 
    | if_statement 
    | for_statement 
    | call_statement 
    | return_statement
    | break_statement
    | continue_statement;

// 7.2 Assignment Statement
// The LHS can be a scalar variable, an array element access (e.g., arr[index]), or a struct field access (e.g., structName.fieldName).
lhs: lhs DOT ID | lhs OSB expression CSB | ID;
// assignment operators :=, +=, -=, *=, /=, and %=.
op_assign: SHORT_DECL | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;
// The RHS is any valid expression, and its value must be compatible with the type of the LHS.
assign_statement: lhs op_assign expression;

// 7.3 If Statement - attention to NEWLINE
else_if_el: ELSE IF OP expression CP OCB list_statement CCB;
else_if_statement:  else_if_el | else_if_el else_if_statement;
else_statement: ELSE OCB list_statement CCB;
if_statement: IF OP expression CP OCB list_statement CCB else_if_statement? else_statement?;

// 7.4 For Statement
for_statement: basic_for_statement | init_for_statement | range_for_statement;

basic_for_statement: FOR expression OCB list_statement CCB;

update_part: ID (SHORT_DECL | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN) expression;
init_part: (ID SHORT_DECL expression) | (VAR ID param_type? ASSIGN expression);
init_for_statement: FOR init_part SEMICOLON expression SEMICOLON update_part OCB list_statement CCB;

range_for_statement: FOR ID COMMA ID SHORT_DECL RANGE expression OCB list_statement CCB;

// 7.5 Break Statement
break_statement: BREAK;

// 7.6 Continue Statement
continue_statement: CONTINUE;

// 7.7 Call Statement
call_statement: func_call | method_call;
method_call: method_alias DOT func_call; 
method_alias: ID | method_alias DOT ID | method_alias OSB expression CSB | method_alias DOT func_call;

// 7.8 Return statement
return_statement: RETURN expression?;

//! ---------------- END OF PARSER ----------------------- */
// TODO ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' STR_CHAR* ('\r\n' | '\n' | EOF) {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[:-1])
    else:
        raise UncloseString(self.text)
};

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL {
    raise IllegalEscape(self.text)
};