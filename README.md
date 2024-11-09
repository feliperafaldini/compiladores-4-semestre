# Implementação de um Compilador com PLY

## Descrição
Este projeto implementa um lexer (analisador léxico) e um parser (analisador sintático) para um subconjunto de uma linguagem fictícia, utilizando as bibliotecas PLY (Python Lex-Yacc). O objetivo do código é identificar e analisar expressões matemáticas, estruturas condicionais (if, else, elif), loops (do-while), atribuições e funções como print em um formato de entrada. O resultado final é a geração de uma Árvore de Sintaxe Abstrata (AST) e a criação de um código a partir dessa AST.

# Estrutura de Código
O código é dividido em duas principais classes: Lexer e Parser, com a ajuda de uma classe auxiliar CodeGenerator para gerar o código a partir da AST.

- Lexer (Analisador Léxico)
O Lexer é responsável por analisar o texto de entrada e separa-lo em tokens (elementos léxicos) que são mais facilmente interpretados pelo parser. Ele usa a biblioteca PLY para definir regras de tokenização com expressões regulares.

Tokens: O lexer reconhece diversos tokens, como identificadores (ID), números (NUMBER), operadores matemáticos (+, -, *, /), operadores de comparação (==, !=, <, >) e operadores lógicos (&&, ||), além de palavras-chave (if, else, while, print).

Funções principais:

- t_ID: Identifica identificadores e palavras-chave.
- t_NUMBER: Identifica números inteiros.
- t_COMMENT: Ignora comentários.
- t_newline: Atualiza o número da linha a cada nova linha.
- t_error: Lida com caracteres inválidos.
-- Método build: Constrói o lexer com o módulo lex.

-- Método test: Testa o lexer com um conjunto de dados de entrada, gerando um arquivo JSON com o resultado da análise léxica.

- Parser (Analisador Sintático)
O Parser é responsável por analisar a sequência de tokens gerada pelo lexer e gerar uma Árvore de Sintaxe Abstrata (AST). Ele usa a biblioteca PLY para definir regras gramaticais e a precedência de operadores.

Regras de Gramática: O parser define várias regras para expressões e sentenças, como:

Expressões Matemáticas: Regras para soma, subtração, multiplicação e divisão.
Comparações: Regras para operadores de comparação como ==, !=, <, >.
Atribuições: Regras para atribuições e operações de atribuição (como += e -=).
Estruturas de Controle: Regras para estruturas condicionais (if, elif, else) e loops (do-while).
Função print: Regra para imprimir valores.
Método build: Constrói o parser com o módulo yacc.

Método test: Testa o parser com um conjunto de dados de entrada e gera uma AST no formato JSON.

# Requisitos
- Python 3.x
- Biblioteca 'ply' para construção do lexer e parser:
```bash
pip install ply
```
