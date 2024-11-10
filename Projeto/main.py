from pathlib import Path

from lexer import Lexer
from parser import Parser
from code_generator import CodeGenerator


class Main:
    def __init__(self):
        self.diretorio_atual = Path.cwd()

        self.operacao = None
        self.data = None

        self.lexer = Lexer()
        self.lexer.build()
        self.parser = Parser()
        self.parser.build()
        self.code_generator = CodeGenerator()
        self.menu()

    def menu(self):
        try:
            while self.operacao == None or self.operacao not in ("1", "2", "3"):
                self.operacao = input(
                    "Escolha uma operação:\n 1 - Lexer\n 2 - Parser\n 3 - CodeGenerator\n"
                )

            match self.operacao:
                case "1":
                    self.menu_lexer()
                case "2":
                    self.menu_parser()
                case "3":
                    self.menu_code_generator()

        except Exception as e:
            print(f"Erro: {e}")

    def menu_lexer(self):
        try:
            while self.data == None:
                self.data = input(
                    "Insira um código para ser transformado em uma lista de tokens: "
                )

            tokens = self.lexer.test(self.data)
            print(tokens)
            print(f"\nResultado salvo em {self.diretorio_atual}\\lexer_result.json")
            input("Aperte qualquer tecla para sair...")

        except Exception as e:
            print(f"Erro: {e}")

    def menu_parser(self):
        try:
            while self.data == None:
                self.data = input("Insira um código para ser transformado em uma AST: ")

            ast = self.parser.test(self.data)
            print(ast)
            print(f"\nResultado salvo {self.diretorio_atual}\\parser_result.json")
            input("Aperte qualquer tecla para sair...")

        except Exception as e:
            print(f"Erro: {e}")

    def menu_code_generator(self):
        try:
            while self.data == None:
                self.data = input(
                    "Insira um código para ser transformado em um código intermediário: "
                )

            ast = self.parser.test(self.data)
            self.code_generator.generate_code(ast)
            self.code_generator.generate_code_output()
            code = self.code_generator.get_code()
            print(code)
            print(f"\nResultado salvo {self.diretorio_atual}\\code_result.txt")
            input("Aperte qualquer tecla para sair...")

        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main = Main()
