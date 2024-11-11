
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftPLUSMINUSleftTIMESDIVIDEleftLESSMOREEQUALrightPLUSASSIGNMINUSASSIGNASSIGNAND ASSIGN COLON COMMA DIVIDE DO ELIF ELSE EQUAL ID IF LBRACE LESS LPAREN MINUS MINUSASSIGN MORE NOTEQUAL NUMBER OR PLUS PLUSASSIGN PRINT RBRACE RPAREN SEMICOLON TIMES WHILEstatements : statement\n        | statements statementstatement : expression SEMICOLONstatement_list : statement\n        | statement statement_listexpression_list : expression\n        | expression_list COMMA expressionstatement : ID ASSIGN expression SEMICOLONstatement : ID PLUSASSIGN expression SEMICOLON\n        | ID MINUSASSIGN expression SEMICOLONexpression : expression PLUS expression\n        | expression MINUS expression\n        | expression TIMES expression\n        | expression DIVIDE expressionexpression : expression EQUAL expression\n        | expression NOTEQUAL expression\n        | expression LESS expression\n        | expression MORE expressionexpression : expression OR expressionexpression : expression AND expressionstatement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE elif_blocks ELSE LBRACE statement_list RBRACE\n        | IF LPAREN expression RPAREN LBRACE statement_list RBRACE elif_blocks\n        | IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE\n        | IF LPAREN expression RPAREN LBRACE statement_list RBRACE\n        elif_blocks : ELIF LPAREN expression RPAREN LBRACE statement_list RBRACE elif_blocks\n        | ELIF LPAREN expression RPAREN LBRACE statement_list RBRACE\n        statement : DO LBRACE statement_list RBRACEstatement : DO LBRACE statement_list RBRACE WHILE LPAREN expression RPAREN SEMICOLONexpression : LPAREN expression RPARENexpression : NUMBERexpression : IDstatement : PRINT LPAREN expression_list RPAREN SEMICOLON'
    
_lr_action_items = {'ID':([0,1,2,6,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,28,29,46,49,50,51,53,56,57,59,62,63,65,70,71,72,73,77,79,80,82,83,],[4,4,-1,27,-2,-3,27,27,27,27,27,27,27,27,27,27,27,27,27,27,4,27,4,-8,-9,-10,-27,27,4,-32,27,-24,-22,4,27,-28,4,-23,-21,4,-26,-25,]),'IF':([0,1,2,10,11,28,46,49,50,51,53,57,59,63,65,70,72,73,77,79,80,82,83,],[5,5,-1,-2,-3,5,5,-8,-9,-10,-27,5,-32,-24,-22,5,-28,5,-23,-21,5,-26,-25,]),'DO':([0,1,2,10,11,28,46,49,50,51,53,57,59,63,65,70,72,73,77,79,80,82,83,],[7,7,-1,-2,-3,7,7,-8,-9,-10,-27,7,-32,-24,-22,7,-28,7,-23,-21,7,-26,-25,]),'PRINT':([0,1,2,10,11,28,46,49,50,51,53,57,59,63,65,70,72,73,77,79,80,82,83,],[8,8,-1,-2,-3,8,8,-8,-9,-10,-27,8,-32,-24,-22,8,-28,8,-23,-21,8,-26,-25,]),'LPAREN':([0,1,2,5,6,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,28,29,46,49,50,51,53,56,57,58,59,62,63,65,67,70,71,72,73,77,79,80,82,83,],[6,6,-1,25,6,29,-2,-3,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,-8,-9,-10,-27,6,6,62,-32,6,-24,-22,71,6,6,-28,6,-23,-21,6,-26,-25,]),'NUMBER':([0,1,2,6,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,28,29,46,49,50,51,53,56,57,59,62,63,65,70,71,72,73,77,79,80,82,83,],[9,9,-1,9,-2,-3,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,-8,-9,-10,-27,9,9,-32,9,-24,-22,9,9,-28,9,-23,-21,9,-26,-25,]),'$end':([1,2,10,11,49,50,51,53,59,63,65,72,77,79,82,83,],[0,-1,-2,-3,-8,-9,-10,-27,-32,-24,-22,-28,-23,-21,-26,-25,]),'SEMICOLON':([3,4,9,27,30,31,32,33,34,35,36,37,38,39,40,41,42,44,55,68,],[11,-31,-30,-31,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,49,50,51,-29,59,72,]),'PLUS':([3,4,9,26,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,48,60,64,75,],[12,-31,-30,12,-31,-11,-12,-13,-14,-15,12,-17,-18,12,12,12,12,12,12,-29,12,12,12,12,]),'MINUS':([3,4,9,26,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,48,60,64,75,],[13,-31,-30,13,-31,-11,-12,-13,-14,-15,13,-17,-18,13,13,13,13,13,13,-29,13,13,13,13,]),'TIMES':([3,4,9,26,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,48,60,64,75,],[14,-31,-30,14,-31,14,14,-13,-14,-15,14,-17,-18,14,14,14,14,14,14,-29,14,14,14,14,]),'DIVIDE':([3,4,9,26,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,48,60,64,75,],[15,-31,-30,15,-31,15,15,-13,-14,-15,15,-17,-18,15,15,15,15,15,15,-29,15,15,15,15,]),'EQUAL':([3,4,9,26,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,48,60,64,75,],[16,-31,-30,16,-31,16,16,16,16,-15,16,-17,-18,16,16,16,16,16,16,-29,16,16,16,16,]),'NOTEQUAL':([3,4,9,26,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,48,60,64,75,],[17,-31,-30,17,-31,-11,-12,-13,-14,-15,17,-17,-18,-19,-20,17,17,17,17,-29,17,17,17,17,]),'LESS':([3,4,9,26,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,48,60,64,75,],[18,-31,-30,18,-31,18,18,18,18,-15,18,-17,-18,18,18,18,18,18,18,-29,18,18,18,18,]),'MORE':([3,4,9,26,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,48,60,64,75,],[19,-31,-30,19,-31,19,19,19,19,-15,19,-17,-18,19,19,19,19,19,19,-29,19,19,19,19,]),'OR':([3,4,9,26,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,48,60,64,75,],[20,-31,-30,20,-31,-11,-12,-13,-14,-15,20,-17,-18,-19,-20,20,20,20,20,-29,20,20,20,20,]),'AND':([3,4,9,26,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,48,60,64,75,],[21,-31,-30,21,-31,-11,-12,-13,-14,-15,21,-17,-18,21,-20,21,21,21,21,-29,21,21,21,21,]),'ASSIGN':([4,],[22,]),'PLUSASSIGN':([4,],[23,]),'MINUSASSIGN':([4,],[24,]),'LBRACE':([7,52,66,69,78,],[28,57,70,73,80,]),'RPAREN':([9,26,27,30,31,32,33,34,35,36,37,38,39,43,44,47,48,60,64,75,],[-30,44,-31,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,52,-29,55,-6,-7,68,78,]),'COMMA':([9,27,30,31,32,33,34,35,36,37,38,39,44,47,48,60,],[-30,-31,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-29,56,-6,-7,]),'RBRACE':([11,45,46,49,50,51,53,54,59,61,63,65,72,74,76,77,79,81,82,83,],[-3,53,-4,-8,-9,-10,-27,-5,-32,63,-24,-22,-28,77,79,-23,-21,82,-26,-25,]),'WHILE':([53,],[58,]),'ELSE':([63,65,82,83,],[66,69,-26,-25,]),'ELIF':([63,82,],[67,67,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,],[1,]),'statement':([0,1,28,46,57,70,73,80,],[2,10,46,46,46,46,46,46,]),'expression':([0,1,6,12,13,14,15,16,17,18,19,20,21,22,23,24,25,28,29,46,56,57,62,70,71,73,80,],[3,3,26,30,31,32,33,34,35,36,37,38,39,40,41,42,43,3,48,3,60,3,64,3,75,3,3,]),'statement_list':([28,46,57,70,73,80,],[45,54,61,74,76,81,]),'expression_list':([29,],[47,]),'elif_blocks':([63,82,],[65,83,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statement','statements',1,'p_statements','parser_code.py',24),
  ('statements -> statements statement','statements',2,'p_statements','parser_code.py',25),
  ('statement -> expression SEMICOLON','statement',2,'p_statement_expression','parser_code.py',33),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser_code.py',38),
  ('statement_list -> statement statement_list','statement_list',2,'p_statement_list','parser_code.py',39),
  ('expression_list -> expression','expression_list',1,'p_expression_list','parser_code.py',47),
  ('expression_list -> expression_list COMMA expression','expression_list',3,'p_expression_list','parser_code.py',48),
  ('statement -> ID ASSIGN expression SEMICOLON','statement',4,'p_statement_assign','parser_code.py',56),
  ('statement -> ID PLUSASSIGN expression SEMICOLON','statement',4,'p_statement_assign_op','parser_code.py',61),
  ('statement -> ID MINUSASSIGN expression SEMICOLON','statement',4,'p_statement_assign_op','parser_code.py',62),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser_code.py',70),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser_code.py',71),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser_code.py',72),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser_code.py',73),
  ('expression -> expression EQUAL expression','expression',3,'p_expression_comparison','parser_code.py',78),
  ('expression -> expression NOTEQUAL expression','expression',3,'p_expression_comparison','parser_code.py',79),
  ('expression -> expression LESS expression','expression',3,'p_expression_comparison','parser_code.py',80),
  ('expression -> expression MORE expression','expression',3,'p_expression_comparison','parser_code.py',81),
  ('expression -> expression OR expression','expression',3,'p_expression_or','parser_code.py',86),
  ('expression -> expression AND expression','expression',3,'p_expression_and','parser_code.py',91),
  ('statement -> IF LPAREN expression RPAREN LBRACE statement_list RBRACE elif_blocks ELSE LBRACE statement_list RBRACE','statement',12,'p_statement_if','parser_code.py',96),
  ('statement -> IF LPAREN expression RPAREN LBRACE statement_list RBRACE elif_blocks','statement',8,'p_statement_if','parser_code.py',97),
  ('statement -> IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE','statement',11,'p_statement_if','parser_code.py',98),
  ('statement -> IF LPAREN expression RPAREN LBRACE statement_list RBRACE','statement',7,'p_statement_if','parser_code.py',99),
  ('elif_blocks -> ELIF LPAREN expression RPAREN LBRACE statement_list RBRACE elif_blocks','elif_blocks',8,'p_statement_elif_blocks','parser_code.py',113),
  ('elif_blocks -> ELIF LPAREN expression RPAREN LBRACE statement_list RBRACE','elif_blocks',7,'p_statement_elif_blocks','parser_code.py',114),
  ('statement -> DO LBRACE statement_list RBRACE','statement',4,'p_statement_do','parser_code.py',124),
  ('statement -> DO LBRACE statement_list RBRACE WHILE LPAREN expression RPAREN SEMICOLON','statement',9,'p_statement_do_while','parser_code.py',129),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser_code.py',134),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser_code.py',139),
  ('expression -> ID','expression',1,'p_expression_id','parser_code.py',144),
  ('statement -> PRINT LPAREN expression_list RPAREN SEMICOLON','statement',5,'p_statement_print','parser_code.py',149),
]
