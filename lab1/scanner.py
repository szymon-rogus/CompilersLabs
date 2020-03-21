import ply.lex as lex

assign_tokens = ( 'ASSIGN', 'ADD_ASSIGN', 'SUBSTRACT_ASSIGN', 'MULTIPLY_ASSIGN', 'DIVIDE_ASSIGN')
relation_tokens = ('LESSER', 'GREATER', 'LESSER_EQUALS', 'GREATER_EQUALS', 'NOT_EQUALS', 'EQUALS')

t_ASSIGN = r'\='
t_ADD_ADDIGN = r'\+='
t_SUBSTRACT_ASSIGN = r'-='
t_MULTIPLY_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='

t_LESSER = r'<'
t_GREATER = r'>'
t_LESSER_EQUALS = r'<='
t_GREATER_EQUALS = r'>='
t_NOT_EQUALS = r'!='
t_EQUALS = r'=='


reserved = {
    'if'    : 'IF',
    'then'  : 'THEN',
    'else'  : 'ELSE',
    'while' : 'WHILE',
    'for'   : 'FOR',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'eye' : 'EYE',
    'zeros' : 'ZEROS',
    'ones' : 'ONES',
    'print' : 'PRINT',
}