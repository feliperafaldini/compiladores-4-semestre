import ply.lex as lex
import json
from lexer_error import LexerError


class Lexer(object):
    # Lista de tokens
    tokens = [
        "ID",  # Identificadores
        "NUMBER",  # Números
        "PLUS",  # +
        "PLUSASSIGN",  # +=
        "MINUS",  # -
        "MINUSASSIGN",  # -=
        "TIMES",  # *
        "DIVIDE",  # /
        "LPAREN",  # (
        "RPAREN",  # )
        "LBRACE",  # {
        "RBRACE",  # }
        "EQUAL",  # ==
        "NOTEQUAL",  # !=
        "ASSIGN",  # =
        "COLON",  # :
        "SEMICOLON",  # ;
        "LESS",  # <
        "MORE",  # >
        "COMMA",  # ,
        "OR",  # ||
        "AND",  # &&
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
    t_PLUSASSIGN = r"\+="
    t_MINUS = r"-"
    t_MINUSASSIGN = r"-="
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
    t_NOTEQUAL = r"!="
    t_ASSIGN = r"="
    t_COMMA = r","
    t_OR = r"\|\|"
    t_AND = r"&&"

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
        raise LexerError(
            f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}", token=t
        )

    # Construção do lexer
    def build(self, **kwargs):
        try:
            self.lexer = lex.lex(module=self, **kwargs)
        except Exception as e:
            print(f"Erro: {e}")

    # Teste do lexer
    def test(self, data):
        try:
            self.lexer.input(data)
            list_tok = []

            while True:
                tok = self.lexer.token()

                if not tok:
                    break

                list_tok.append(tok)

            json_output = [
                {"type": tok.type, "value": tok.value, "lineno": tok.lineno}
                for tok in list_tok
            ]

            with open("lexer_result.json", "w", encoding="utf-8") as f:
                json.dump(json_output, f, ensure_ascii=False, indent=4)

            return list_tok

        except LexerError as e:
            print(f"Erro: {e}")
            raise


if __name__ == "__main__":
    lexer = Lexer()
    lexer.build()
    result = lexer.test(
        """  x = 10; 
                y= 1;
                do { 
                    x -= 1;
                } while ( x > 1 );
                if (x != y || x == y) {
                    print( x ); 
                } elif (x == y && x != y) {
                    print( y ); 
                } else {
                    print( x , y );
                }
            """
    )
    print(result)
