
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASSIGNADD_ASSIGNSUBSTRACT_ASSIGNMULTIPLY_ASSIGNDIVIDE_ASSIGNleftPLUSMINUSleftMPLUSMMINUSleftTIMESDIVIDEleftMTIMESMDIVIDEADD_ASSIGN ASSIGN BREAK COMMA COMMENT CONTINUE DIVIDE DIVIDE_ASSIGN ELSE EQUALS EYE FLOAT FOR GREATER GREATER_EQUALS ID IF INT LBRACE LBRACKET LESSER LESSER_EQUALS LSQUARE MDIVIDE MINUS MMINUS MPLUS MTIMES MULTIPLY_ASSIGN NOT_EQUALS ONES PLUS PRINT RANGE RBRACE RBRACKET RETURN RSQUARE SEMICOLON STRING SUBSTRACT_ASSIGN THEN TIMES TRANSPOSITION WHILE ZEROSPROGRAM : EXPRESSIONEXPRESSION : LBRACKET EXPRESSION RBRACKETEXPRESSION : INT\n                  | FLOATEXPRESSION : IDEXPRESSION : EXPRESSION PLUS EXPRESSION\n                  | EXPRESSION MINUS EXPRESSION\n                  | EXPRESSION MPLUS EXPRESSION\n                  | EXPRESSION MMINUS EXPRESSIONEXPRESSION : EXPRESSION TIMES EXPRESSION\n                  | EXPRESSION DIVIDE EXPRESSION\n                  | EXPRESSION MTIMES EXPRESSION\n                  | EXPRESSION MDIVIDE EXPRESSIONEXPRESSION : EXPRESSION ASSIGN EXPRESSION\n                  | EXPRESSION ADD_ASSIGN EXPRESSION\n                  | EXPRESSION SUBSTRACT_ASSIGN EXPRESSION\n                  | EXPRESSION MULTIPLY_ASSIGN EXPRESSION\n                  | EXPRESSION DIVIDE_ASSIGN EXPRESSION'
    
_lr_action_items = {'LBRACKET':([0,3,7,8,9,10,11,12,13,14,15,16,17,18,19,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'INT':([0,3,7,8,9,10,11,12,13,14,15,16,17,18,19,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'FLOAT':([0,3,7,8,9,10,11,12,13,14,15,16,17,18,19,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'ID':([0,3,7,8,9,10,11,12,13,14,15,16,17,18,19,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'$end':([1,2,4,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-2,]),'PLUS':([2,4,5,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[7,-3,-4,-5,7,-6,-7,-8,-9,-10,-11,-12,-13,7,7,7,7,7,-2,]),'MINUS':([2,4,5,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[8,-3,-4,-5,8,-6,-7,-8,-9,-10,-11,-12,-13,8,8,8,8,8,-2,]),'MPLUS':([2,4,5,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[9,-3,-4,-5,9,9,9,-8,-9,-10,-11,-12,-13,9,9,9,9,9,-2,]),'MMINUS':([2,4,5,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[10,-3,-4,-5,10,10,10,-8,-9,-10,-11,-12,-13,10,10,10,10,10,-2,]),'TIMES':([2,4,5,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[11,-3,-4,-5,11,11,11,11,11,-10,-11,-12,-13,11,11,11,11,11,-2,]),'DIVIDE':([2,4,5,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[12,-3,-4,-5,12,12,12,12,12,-10,-11,-12,-13,12,12,12,12,12,-2,]),'MTIMES':([2,4,5,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[13,-3,-4,-5,13,13,13,13,13,13,13,-12,-13,13,13,13,13,13,-2,]),'MDIVIDE':([2,4,5,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[14,-3,-4,-5,14,14,14,14,14,14,14,-12,-13,14,14,14,14,14,-2,]),'ASSIGN':([2,4,5,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[15,-3,-4,-5,15,-6,-7,-8,-9,-10,-11,-12,-13,15,15,15,15,15,-2,]),'ADD_ASSIGN':([2,4,5,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[16,-3,-4,-5,16,-6,-7,-8,-9,-10,-11,-12,-13,16,16,16,16,16,-2,]),'SUBSTRACT_ASSIGN':([2,4,5,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[17,-3,-4,-5,17,-6,-7,-8,-9,-10,-11,-12,-13,17,17,17,17,17,-2,]),'MULTIPLY_ASSIGN':([2,4,5,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[18,-3,-4,-5,18,-6,-7,-8,-9,-10,-11,-12,-13,18,18,18,18,18,-2,]),'DIVIDE_ASSIGN':([2,4,5,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[19,-3,-4,-5,19,-6,-7,-8,-9,-10,-11,-12,-13,19,19,19,19,19,-2,]),'RBRACKET':([4,5,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,],[-3,-4,-5,34,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'EXPRESSION':([0,3,7,8,9,10,11,12,13,14,15,16,17,18,19,],[2,20,21,22,23,24,25,26,27,28,29,30,31,32,33,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('PROGRAM -> EXPRESSION','PROGRAM',1,'p_program','Mparser.py',26),
  ('EXPRESSION -> LBRACKET EXPRESSION RBRACKET','EXPRESSION',3,'p_expression_brackets','Mparser.py',31),
  ('EXPRESSION -> INT','EXPRESSION',1,'p_expression_number','Mparser.py',36),
  ('EXPRESSION -> FLOAT','EXPRESSION',1,'p_expression_number','Mparser.py',37),
  ('EXPRESSION -> ID','EXPRESSION',1,'p_expression_id','Mparser.py',42),
  ('EXPRESSION -> EXPRESSION PLUS EXPRESSION','EXPRESSION',3,'p_expression_sum','Mparser.py',53),
  ('EXPRESSION -> EXPRESSION MINUS EXPRESSION','EXPRESSION',3,'p_expression_sum','Mparser.py',54),
  ('EXPRESSION -> EXPRESSION MPLUS EXPRESSION','EXPRESSION',3,'p_expression_sum','Mparser.py',55),
  ('EXPRESSION -> EXPRESSION MMINUS EXPRESSION','EXPRESSION',3,'p_expression_sum','Mparser.py',56),
  ('EXPRESSION -> EXPRESSION TIMES EXPRESSION','EXPRESSION',3,'p_expression_mul','Mparser.py',68),
  ('EXPRESSION -> EXPRESSION DIVIDE EXPRESSION','EXPRESSION',3,'p_expression_mul','Mparser.py',69),
  ('EXPRESSION -> EXPRESSION MTIMES EXPRESSION','EXPRESSION',3,'p_expression_mul','Mparser.py',70),
  ('EXPRESSION -> EXPRESSION MDIVIDE EXPRESSION','EXPRESSION',3,'p_expression_mul','Mparser.py',71),
  ('EXPRESSION -> EXPRESSION ASSIGN EXPRESSION','EXPRESSION',3,'p_expression_assignment','Mparser.py',79),
  ('EXPRESSION -> EXPRESSION ADD_ASSIGN EXPRESSION','EXPRESSION',3,'p_expression_assignment','Mparser.py',80),
  ('EXPRESSION -> EXPRESSION SUBSTRACT_ASSIGN EXPRESSION','EXPRESSION',3,'p_expression_assignment','Mparser.py',81),
  ('EXPRESSION -> EXPRESSION MULTIPLY_ASSIGN EXPRESSION','EXPRESSION',3,'p_expression_assignment','Mparser.py',82),
  ('EXPRESSION -> EXPRESSION DIVIDE_ASSIGN EXPRESSION','EXPRESSION',3,'p_expression_assignment','Mparser.py',83),
]
