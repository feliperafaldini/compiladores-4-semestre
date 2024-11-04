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

# 