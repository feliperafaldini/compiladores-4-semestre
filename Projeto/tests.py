import unittest
from lexer_code import Lexer
from lexer_error import LexerError

from parser_code import Parser
from parser_error import ParserError


class TestLexer(unittest.TestCase):
    def setUp(self):
        self.lexer = Lexer()
        self.lexer.build()

    def test_tokens_1(self):
        data = "x = 10;"
        result = self.lexer.test(data)

        expected_tokens = [
            {"type": "ID", "value": "x", "lineno": 1},
            {"type": "ASSIGN", "value": "=", "lineno": 1},
            {"type": "NUMBER", "value": 10, "lineno": 1},
            {"type": "SEMICOLON", "value": ";", "lineno": 1},
        ]

        if result is not None:
            self.assertEqual(len(result), len(expected_tokens))
            for expected, actual in zip(expected_tokens, result):
                self.assertEqual(expected["type"], actual.type)
                self.assertEqual(expected["value"], actual.value)

    def test_tokens_2(self):
        data = "if (x > 10) { y = 1 }"
        result = self.lexer.test(data)

        expected_tokens = [
            {"type": "IF", "value": "if", "lineno": 1},
            {"type": "LPAREN", "value": "(", "lineno": 1},
            {"type": "ID", "value": "x", "lineno": 1},
            {"type": "MORE", "value": ">", "lineno": 1},
            {"type": "NUMBER", "value": 10, "lineno": 1},
            {"type": "RPAREN", "value": ")", "lineno": 1},
            {"type": "LBRACE", "value": "{", "lineno": 1},
            {"type": "ID", "value": "y", "lineno": 1},
            {"type": "ASSIGN", "value": "=", "lineno": 1},
            {"type": "NUMBER", "value": 1, "lineno": 1},
            {"type": "RBRACE", "value": "}", "lineno": 1},
        ]

        if result is not None:
            self.assertEqual(len(result), len(expected_tokens))
            for expected, actual in zip(expected_tokens, result):
                self.assertEqual(expected["type"], actual.type)
                self.assertEqual(expected["value"], actual.value)

    def test_tokens_3(self):
        data = "do { x += 1 } while ( x < 10 )"
        result = self.lexer.test(data)

        expected_tokens = [
            {"type": "DO", "value": "do", "lineno": 1},
            {"type": "LBRACE", "value": "{", "lineno": 1},
            {"type": "ID", "value": "x", "lineno": 1},
            {"type": "PLUSASSIGN", "value": "+=", "lineno": 1},
            {"type": "NUMBER", "value": 1, "lineno": 1},
            {"type": "RBRACE", "value": "}", "lineno": 1},
            {"type": "WHILE", "value": "while", "lineno": 1},
            {"type": "LPAREN", "value": "(", "lineno": 1},
            {"type": "ID", "value": "x", "lineno": 1},
            {"type": "LESS", "value": "<", "lineno": 1},
            {"type": "NUMBER", "value": 10, "lineno": 1},
            {"type": "RPAREN", "value": ")", "lineno": 1},
        ]

        if result is not None:
            self.assertEqual(len(result), len(expected_tokens))
            for expected, actual in zip(expected_tokens, result):
                self.assertEqual(expected["type"], actual.type)
                self.assertEqual(expected["value"], actual.value)

    def test_unvalid_token_1(self):
        data = "x = 10 @"

        with self.assertRaises(LexerError) as context:
            self.lexer.test(data)

        self.assertIn("Caractere ilegal", str(context.exception))

    def test_unvalid_token_2(self):
        data = "~if ( x < 10) { x += 1 }"

        with self.assertRaises(LexerError) as context:
            self.lexer.test(data)

        self.assertIn("Caractere ilegal", str(context.exception))

    def test_unvalid_token_3(self):
        data = " x = 'x' "

        with self.assertRaises(LexerError) as context:
            self.lexer.test(data)

        self.assertIn("Caractere ilegal", str(context.exception))


class TestParser(unittest.TestCase):
    def setUp(self):
        self.lexer = Lexer()
        self.lexer.build()
        self.parser = Parser()
        self.parser.build()

    def test_valid_syntax_1(self):
        data = "x = 10;"
        result = self.parser.test(data)

        self.assertIsNotNone(result)

    def test_valid_syntax_2(self):
        data = "if ( x < 10 ) { x += 1; }"
        result = self.parser.test(data)

        self.assertIsNotNone(result)

    def test_valid_syntax_3(self):
        data = "do { x += 1; } while ( x < 10 );"
        result = self.parser.test(data)

        self.assertIsNotNone(result)

    def test_invalid_syntax_1(self):
        data = "x 10;"

        with self.assertRaises(ParserError) as context:
            self.parser.test(data)

        self.assertIn("Erro sintático encontrado: ", str(context.exception))

    def test_invalid_syntax_2(self):
        data = "x = 1"

        with self.assertRaises(ParserError) as context:
            self.parser.test(data)

        self.assertIn("Erro sintático encontrado: ", str(context.exception))

    def test_invalid_syntax_3(self):
        data = "fi ( x < 10; )"

        with self.assertRaises(ParserError) as context:
            self.parser.test(data)

        self.assertIn("Erro sintático encontrado: ", str(context.exception))


if __name__ == "__main__":
    unittest.main()
