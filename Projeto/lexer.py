import os
import ply.lex as lex


class Lexer(object):
    # Lista de tokens
    tokens = [
        "ID",  # Identificadores
        "NUMBER",  # Números
        "PLUS",  # +
        "MINUS",  # -
        "TIMES",  # *
        "DIVIDE",  # /
        "LPAREN",  # (
        "RPAREN",  # )
        "LBRACE",  # {
        "RBRACE",  # }
        "EQUAL",  # ==
        "ASSIGN",  # =
        "COLON",  # :
        "SEMICOLON",  # ;
        "LESS",  # <
        "MORE",  # >
    ]

    # Palavras-chave
    keywords = {
        "if": "IF",
        "else": "ELSE",
        "elif": "ELIF",
        "do": "DO",
        "while": "WHILE",
        "print": "PRINT",
    }

    # Adiciona palavras-chave à lista de tokens
    tokens = tokens + list(keywords.values())

    # Expressões regulares para tokens
    t_PLUS = r"\+"
    t_MINUS = r"-"
    t_TIMES = r"\*"
    t_DIVIDE = r"/"
    t_LPAREN = r"\("
    t_RPAREN = r"\)"
    t_LBRACE = r"\{"
    t_RBRACE = r"\}"
    t_COLON = r":"
    t_SEMICOLON = r";"
    t_LESS = r"<"
    t_MORE = r">"
    t_EQUAL = r"=="
    t_ASSIGN = r"="

    # Função para identificadores e palavras-chave
    def t_ID(self, t):
        r"[a-zA-Z_][a-zA-Z_0-9]*"
        t.type = self.keywords.get(
            t.value, "ID"
        )  # Define o tipo de token como palavra-chave ou ID
        return t

    # Função para números
    def t_NUMBER(self, t):
        r"\d+"
        t.value = int(t.value)  # Converte o valor para inteiro
        return t

    # Função para comentários
    def t_COMMENT(self, t):
        r"\#.*"
        pass

    # Ignorar espaços e tabulações
    t_ignore = " \t"

    # Quebra de linhas
    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    # Função para erros léxicos
    def t_error(self, t):
        print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
        t.lexer.skip(1)

    # Construção do lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Teste
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)


if __name__ == "__main__":
    lexer = Lexer()
    lexer.build()
    lexer.test("""x=1; do {x=x+1;} while (x<3)""")
