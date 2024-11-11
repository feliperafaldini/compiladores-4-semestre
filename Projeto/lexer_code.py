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
        """
        Identifica um identificador.
        O identificador pode começar com uma letra (a-z, A-Z) ou um underscore (_),
        seguido de zero ou mais letras, dígitos ou underscores.

        Parâmetros t:
            O token a ser processado.
        Returns:
            O token processado.
        """
        r"[a-zA-Z_][a-zA-Z_0-9]*"
        t.type = self.keywords.get(
            t.value, "ID"
        )  # Define o tipo de token como palavra-chave ou ID
        return t

    # Função para números
    def t_NUMBER(self, t):
        """
        Função para identificar números.
        O token NUMBER é qualquer sequência de dígitos.

        Parâmetros t:
            O token a ser processado.
        Returns:
            O token processado.
        """
        r"\d+"
        t.value = int(t.value)  # Converte o valor para inteiro
        return t

    # Função para comentários
    def t_COMMENT(self, t):
        """
        Ignora comentarios que comecam com "#".

        Parâmetros t:
            O token a ser processado.
        """
        r"\#.*"
        pass

    # Ignorar espaços e tabulações
    t_ignore = " \t"

    # Quebra de linhas
    def t_newline(self, t):
        """
        Função para quebra de linhas.
        A quebra de linha é definida como uma ou mais ocorrências do caractere de
        quebra de linha (\n).

        Parâmetros t:
            O token a ser processado.
        """
        r"\n+"
        t.lexer.lineno += len(t.value)  # Incrementa o contador de linhas

    # Função para erros léxicos
    def t_error(self, t):
        """
        Função para erros léxicos.
        Lança uma exceção quando um caractere ilegal é encontrado.

        Parâmetros t:
            O token a ser processado.
        """
        raise LexerError(
            f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}", token=t
        )

    # Construção do lexer
    def build(self, **kwargs):
        """
        Constrói o lexer.

        Parâmetros:
            kwargs: Parâmetros adicionais para o construtor do lexer.

        Lança:
            Exception: Caso haja um erro no construtor do lexer.
        """
        try:
            self.lexer = lex.lex(module=self, **kwargs)
        except Exception as e:
            print(f"Erro: {e}")

    # Teste do lexer
    def test(self, data):
        """
        Testa o lexer processando a entrada de dados e gerando uma lista de tokens.

        Parâmetros:
            data: Entrada de dados tipo string para ser tokenizada

        Returns:
            list_tok: Lista de tokens encontrados no código de entrada.

        Raises:
            LexerError: Caso haja algum caractere ilegal.
        """
        try:
            self.lexer.input(data)  # Entrada do código no lexer
            list_tok = []

            while True:
                tok = self.lexer.token()  # Pega o novo token

                if not tok:  # Caso não tenham mais tokens quebra o loop
                    break

                list_tok.append(tok)  # Adiciona o token a lista de tokens

            # Converte os tokens em um dicionário em JSON
            json_output = [
                {"type": tok.type, "value": tok.value, "lineno": tok.lineno}
                for tok in list_tok
            ]

            # Exporta o dicionário JSON para outro arquivo
            with open("lexer_result.json", "w", encoding="utf-8") as f:
                json.dump(json_output, f, ensure_ascii=False, indent=4)

            return list_tok

        except LexerError as e:
            print(f"Erro: {e}")  # Print da mensagem de erro
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
