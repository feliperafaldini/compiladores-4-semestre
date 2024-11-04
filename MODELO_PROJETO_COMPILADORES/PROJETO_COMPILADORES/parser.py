import ply.yacc as yacc
from lexer import tokens  # Importa os tokens do lexer

# Precedência dos operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Regras gramaticais
def p_statement_assign(p):
    'statement : ID ASSIGN expression SEMICOLON'
    p[0] = ('assign', p[1], p[3])

def p_statement_expr(p):
    'statement : expression SEMICOLON'
    p[0] = ('expr', p[1])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = ('id', p[1])

# Tratamento de erros sintáticos
def p_error(p):
    print("Erro sintático encontrado")

# Construção do parser
parser = yacc.yacc()

# Teste do parser
data = "x = 3 + 4 * (10 - 2);"
result = parser.parse(data)
print(result)