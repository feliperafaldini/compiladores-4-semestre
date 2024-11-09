import ply.yacc as yacc
import json
from lexer import Lexer
from parser_error import ParserError

from codegenerator import CodeGenerator


class Parser(object):
    # Importação dos tokens
    tokens = Lexer.tokens

    # Precedência dos operadores
    precedence = (
        ("left", "OR"),
        ("left", "AND"),
        ("left", "PLUS", "MINUS"),
        ("left", "TIMES", "DIVIDE"),
        ("left", "LESS", "MORE", "EQUAL"),
        ("right", "PLUSASSIGN", "MINUSASSIGN", "ASSIGN"),
    )

    # Regras gramaticais
    ## Regra de multiplos statements
    def p_statements(self, p):
        """statements : statement
        | statements statement"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    ## Regra de expressions
    def p_statement_expression(self, p):
        """statement : expression SEMICOLON"""
        p[0] = ("expression", p[1])

    ## Regra para lista de statements dentro de um bloco
    def p_statement_list(self, p):
        """statement_list : statement
        | statement statement_list"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[2]

    ## Regra para lista de expressions dentro de um bloco
    def p_expression_list(self, p):
        """expression_list : expression
        | expression_list COMMA expression"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    ## Regra de Assign "="
    def p_statement_assign(self, p):
        """statement : ID ASSIGN expression SEMICOLON"""
        p[0] = ("assign", p[1], p[3])

    ## Regra de expressions de soma e subtração ao valor anterior
    def p_statement_assign_op(self, p):
        """statement : ID PLUSASSIGN expression SEMICOLON
        | ID MINUSASSIGN expression SEMICOLON"""
        if p[2] == "+=":
            p[0] = ("assign_op", p[1], "+=", p[3])
        elif p[2] == "-=":
            p[0] = ("assign_op", p[1], "-=", p[3])

    ## Regra de expressions matemáticas
    def p_expression_binop(self, p):
        """expression : expression PLUS expression
        | expression MINUS expression
        | expression TIMES expression
        | expression DIVIDE expression"""
        p[0] = (p[2], p[1], p[3])

    ## Regra de expressions de comparação
    def p_expression_comparison(self, p):
        """expression : expression EQUAL expression
        | expression NOTEQUAL expression
        | expression LESS expression
        | expression MORE expression"""
        p[0] = ("comparison", p[2], p[1], p[3])

    ## Regra de operação OR
    def p_expression_or(self, p):
        """expression : expression OR expression"""
        p[0] = ("or", p[1], p[3])

    ## Regra de operação AND
    def p_expression_and(self, p):
        """expression : expression AND expression"""
        p[0] = ("and", p[1], p[3])

    ## Regra para Bloco de Código condicional if(n){x} elif(n){x} else(n){x}
    def p_statement_if(self, p):
        """statement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE elif_blocks ELSE LBRACE statement_list RBRACE
        | IF LPAREN expression RPAREN LBRACE statement_list RBRACE elif_blocks
        | IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE
        | IF LPAREN expression RPAREN LBRACE statement_list RBRACE
        """

        if len(p) == 8:
            p[0] = ("if", p[3], p[6])
        elif len(p) == 9:
            p[0] = ("if_elif", p[3], p[6], p[8])
        elif len(p) == 12:
            p[0] = ("if_else", p[3], p[6], p[10])
        elif len(p) == 13:
            p[0] = ("if_elif_else", p[3], p[6], p[8], p[12])

    ## Regra para Bloco de Código condicional elif(n){x}
    def p_statement_elif_blocks(self, p):
        """elif_blocks : ELIF LPAREN expression RPAREN LBRACE statement_list RBRACE elif_blocks
        | ELIF LPAREN expression RPAREN LBRACE statement_list RBRACE
        """

        if len(p) == 8:
            p[0] = [("elif", p[3], p[6])]
        else:
            p[0] = [("elif", p[3], p[6])] + p[8]

    ## Regra para Bloco de Código de repetição do {}
    def p_statement_do(self, p):
        """statement : DO LBRACE statement_list RBRACE"""
        p[0] = ("do", p[3])

    ## Regra para Bloco de Código de repetição do {} while ()
    def p_statement_do_while(self, p):
        """statement : DO LBRACE statement_list RBRACE WHILE LPAREN expression RPAREN SEMICOLON"""
        p[0] = ("do_while", p[3], p[7])

    ## Regra de expressions entre parenteses
    def p_expression_group(self, p):
        "expression : LPAREN expression RPAREN"
        p[0] = ("group-expression", p[2])

    ## Regra para expressions relacionando a números
    def p_expression_number(self, p):
        "expression : NUMBER"
        p[0] = ("number-expression", p[1])

    ## Regra para expressions relacionado a variáveis
    def p_expression_id(self, p):
        "expression : ID"
        p[0] = ("id", p[1])

    ## Regra para função Print
    def p_statement_print(self, p):
        "statement : PRINT LPAREN expression_list RPAREN SEMICOLON"
        p[0] = ("print", p[3])

    # Tratamento de erros sintáticos
    def p_error(self, p):
        if p:
            raise ParserError(
                f"Erro sintático encontrado: Token {p.type}, com o valor '{p.value}' na linha {p.lineno}",
                token=p,
            )

        else:
            raise ParserError(f"Erro sintático encontrado: Erro na entrada")

    # Construção do parser
    def build(self, **kwargs):
        try:
            self.parser = yacc.yacc(module=self, **kwargs)

        except Exception as e:
            print(f"Erro: {e}")

    # Teste do parser
    def test(self, data):
        try:
            lexer = Lexer()
            lexer.build()
            lexer.lexer.input(data)
            result = self.parser.parse(data, lexer=lexer.lexer)

            with open("parser_result.json", "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=True)

            return result

        except ParserError as e:
            print(f"Erro: {e}")
            raise


if __name__ == "__main__":
    parser = Parser()
    parser.build(debug=True)
    data = """  x = 10; 
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
    ast = parser.test(data)
    generator = CodeGenerator()
    generator.generate_code(ast)
    print(generator.get_code())