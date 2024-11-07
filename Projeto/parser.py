import ply.yacc as yacc
from lexer import Lexer


class Parser(object):
    # Importação dos tokens
    tokens = Lexer.tokens

    # Precedência dos operadores
    precedence = (
        ("left", "PLUS", "MINUS"),
        ("left", "TIMES", "DIVIDE"),
        ("left", "LESS", "MORE", "EQUAL"),
    )

    # Regras gramaticais
    def p_statement_assign(self, p):
        "statement : ID ASSIGN expression SEMICOLON"
        p[0] = ("assign", p[1], p[3])

    def p_statement_expr(self, p):
        "statement : expression SEMICOLON"
        p[0] = ("expr", p[1])

    def p_expression_binop(self, p):
        """expression : expression PLUS expression
        | expression MINUS expression
        | expression TIMES expression
        | expression DIVIDE expression
        | expression LESS expression
        | expression MORE expression
        | expression EQUAL expression"""
        p[0] = (p[2], p[1], p[3])

    def p_expression_group(self, p):
        "expression : LPAREN expression RPAREN"
        p[0] = p[2]

    def p_expression_number(self, p):
        "expression : NUMBER"
        p[0] = p[1]

    def p_expression_id(self, p):
        "expression : ID"
        p[0] = ("id", p[1])

    def p_statement_do(self, p):
        """statement : DO LBRACE statement_list RBRACE"""
        p[0] = ("do", p[3])

    def p_statement_do_while(self, p):
        """statement : DO LBRACE statement_list RBRACE WHILE LPAREN expression RPAREN SEMICOLON"""
        p[0] = ("do_while", p[3], p[7])

    def p_statement_list(self, p):
        """statement_list : statement
        | statement statement_list"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[2]

    def p_statement_print(self, p):
        "statement : PRINT LPAREN expression RPAREN"
        p[0] = ("print", p[3])

    def p_statement_if(self, p):
        """statement : IF LPAREN expression RPAREN LBRACE statement RBRACE
        | IF LPAREN expression RPAREN RPAREN statement RBRACE ELIF LPAREN expression RPAREN RPAREN statement RBRACE
        | IF LPAREN expression RPAREN RPAREN statement RBRACE ELSE RPAREN statement RBRACE
        | IF LPAREN expression RPAREN RPAREN statement RBRACE ELIF LPAREN expression RPAREN RPAREN statement RBRACE ELSE COLON statement RBRACE
        """

        if len(p) == 6:
            p[0] = ("if", p[3], p[5], None, None)
        elif len(p) == 10:
            p[0] = ("if", p[3], p[5], ("elif", p[7], p[9]), None)
        elif len(p) == 12:
            p[0] = ("if", p[3], p[5], ("elif", p[7], p[9]), p[11])
        elif len(p) == 14:
            p[0] = (
                "if",
                p[3],
                p[5],
                [("elif", p[7], p[9]), ("elif", p[11], p[13])],
                p[15],
            )

    # Tratamento de erros sintáticos
    def p_error(self, p):
        if p:
            print(
                f"Erro sintático encontrado: Token {p.type}, com o valor '{p.value}' na linha {p.lineno}"
            )
        else:
            print(f"Erro sintático encontrado: Erro na entrada")

    # Construção do parser
    def build(self):
        self.parser = yacc.yacc(module=self)

    # Teste do parser
    def test(self, data):
        lexer = Lexer()
        lexer.build()
        lexer.lexer.input(data)
        result = self.parser.parse(data, lexer=lexer.lexer)
        print(result)


if __name__ == "__main__":
    parser = Parser()
    parser.build()
    data = """x = 1; do {x=x+1;} while (1+1);"""
    parser.test(data)
