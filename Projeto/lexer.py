import ply.lex as lex

# Lista de tokens
tokens = [
    'ID',        # Identificadores
    'NUMBER',    # Números
    'PLUS',      # +
    'MINUS',     # -
    'TIMES',     # *
    'DIVIDE',    # /
    'LPAREN',    # (
    'RPAREN',    # )
    'ASSIGN',    # =
    'SEMICOLON', # ;
    'IF',        # Condicional
    'ELIF',      # Condicional
    'ELSE',      # Condicional
    'WHILE',     # Enquanto
]

# Palavras-chave
keywords = {
    'if' : 'IF',
    'else': 'ElSE',
    'elif': 'ELIF',
    'while': 'WHILE',
    'print': 'PRINT',
}

# Adiciona palavras-chave à lista de tokens
tokens = tokens + list(keywords.values())

# Expressões regulares para tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_SEMICOLON = r';'
t_IF = r'if'
t_ELIF = r'elif'
r_ELSE = r'else'
r_WHILE = r'while'

# Função para identificadores e palavras-chave
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'ID')  # Define o tipo de token como palavra-chave ou ID
    return t

# Função para números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Converte o valor para inteiro
    return t

# Ignorar espaços e tabulações
t_ignore = ' \t'

# Função para erros léxicos
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()

# Teste do lexer
data = "x = 3 + 4 * (10 - 2);"
lexer.input(data)

for tok in lexer:
    print(tok)