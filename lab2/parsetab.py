
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIFnonassocLESSERGREATEREQUALSNOT_EQUALSLESSER_EQUALSGREATER_EQUALSELSEleftPLUSMINUSMPLUSMMINUSleftTIMESDIVIDEMTIMESMDIVIDEleftUMINUSnonassocTRANSPOSITIONADD_ASSIGN ASSIGN BREAK COMMA COMMENT CONTINUE DIVIDE DIVIDE_ASSIGN ELSE EQUALS EYE FLOAT FOR GREATER GREATER_EQUALS ID IF INT LBRACE LBRACKET LESSER LESSER_EQUALS LSQUARE MDIVIDE MINUS MMINUS MPLUS MTIMES MULTIPLY_ASSIGN NOT_EQUALS ONES PLUS PRINT RANGE RBRACE RBRACKET RETURN RSQUARE SEMICOLON STRING SUBSTRACT_ASSIGN THEN TIMES TRANSPOSITION WHILE ZEROSPROGRAM : CODE_BLOCK\n        CODE_BLOCK : CODE_BLOCK LBRACE CODE_BLOCK RBRACE\n              | LBRACE CODE_BLOCK RBRACE\n        \n        CODE_BLOCK : CODE_BLOCK instruction\n              | instruction\n        \n        instruction : statement SEMICOLON\n                    | if_statement\n                    | while_statement\n                    | for_statement\n        \n        statement : assignment\n                  | keyword\n        \n        assignment : variable assignment_operator expression\n        \n        variable : ID\n                 | variable_attribute\n        \n        variable_attribute : ID LSQUARE sequence RSQUARE\n        \n        sequence : sequence COMMA expression\n                 | expression\n        \n        value : FLOAT\n              | INT\n              | STRING\n              | matrix\n              | variable_attribute\n        \n        matrix : LSQUARE rows RSQUARE\n        \n        rows : rows SEMICOLON sequence\n             | sequence\n        \n        expression : value\n        expression : ID\n        expression : MINUS expression %prec UMINUS\n        \n        expression : ID TRANSPOSITION\n        \n        expression : LBRACKET expression RBRACKET TRANSPOSITION\n        \n        expression : LBRACKET expression RBRACKET\n        \n        expression : expression PLUS expression\n                   | expression MINUS expression\n                   | expression TIMES expression\n                   | expression DIVIDE expression\n                   | expression MPLUS expression\n                   | expression MMINUS expression\n                   | expression MTIMES expression\n                   | expression MDIVIDE expression\n        \n        expression : function LBRACKET expression RBRACKET\n                   | function LBRACKET sequence RBRACKET\n        \n        keyword : PRINT sequence\n        \n        keyword : BREAK\n        \n        keyword : CONTINUE\n        \n        keyword : RETURN expression\n        relation : expression logic_operator expressionbody : LBRACE CODE_BLOCK RBRACE\n                | instruction\n        if_statement : IF LBRACKET relation RBRACKET body %prec IF\n        \n        if_statement : IF LBRACKET relation RBRACKET body ELSE body\n        while_statement : WHILE LBRACKET relation RBRACKET bodyfor_statement : FOR ID ASSIGN range bodyrange : expression RANGE expression RANGE expression\n                 | expression RANGE expression\n        assignment_operator : ASSIGN\n                            | ADD_ASSIGN\n                            | SUBSTRACT_ASSIGN\n                            | MULTIPLY_ASSIGN\n                            | DIVIDE_ASSIGN\n        \n        logic_operator : LESSER\n                       | GREATER\n                       | EQUALS\n                       | NOT_EQUALS\n                       | LESSER_EQUALS\n                       | GREATER_EQUALS\n        \n        function : EYE\n                 | ZEROS\n                 | ONES\n        '
    
_lr_action_items = {'LBRACE':([0,2,3,4,6,7,8,21,22,23,24,37,38,42,43,44,45,46,52,53,69,70,75,76,84,85,87,89,90,91,92,93,94,95,96,97,100,102,103,104,106,107,109,110,111,113,114,115,116,117,119,],[3,21,3,-5,-7,-8,-9,3,-4,21,-6,-26,-27,-18,-19,-20,-21,-22,21,-3,-29,-28,-2,103,103,103,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-49,3,-48,-51,-52,-30,-40,-41,103,21,-54,-50,-47,-53,]),'IF':([0,2,3,4,6,7,8,21,22,23,24,37,38,42,43,44,45,46,52,53,69,70,75,76,84,85,87,89,90,91,92,93,94,95,96,97,100,102,103,104,106,107,109,110,111,113,114,115,116,117,119,],[11,11,11,-5,-7,-8,-9,11,-4,11,-6,-26,-27,-18,-19,-20,-21,-22,11,-3,-29,-28,-2,11,11,11,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-49,11,-48,-51,-52,-30,-40,-41,11,11,-54,-50,-47,-53,]),'WHILE':([0,2,3,4,6,7,8,21,22,23,24,37,38,42,43,44,45,46,52,53,69,70,75,76,84,85,87,89,90,91,92,93,94,95,96,97,100,102,103,104,106,107,109,110,111,113,114,115,116,117,119,],[12,12,12,-5,-7,-8,-9,12,-4,12,-6,-26,-27,-18,-19,-20,-21,-22,12,-3,-29,-28,-2,12,12,12,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-49,12,-48,-51,-52,-30,-40,-41,12,12,-54,-50,-47,-53,]),'FOR':([0,2,3,4,6,7,8,21,22,23,24,37,38,42,43,44,45,46,52,53,69,70,75,76,84,85,87,89,90,91,92,93,94,95,96,97,100,102,103,104,106,107,109,110,111,113,114,115,116,117,119,],[13,13,13,-5,-7,-8,-9,13,-4,13,-6,-26,-27,-18,-19,-20,-21,-22,13,-3,-29,-28,-2,13,13,13,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-49,13,-48,-51,-52,-30,-40,-41,13,13,-54,-50,-47,-53,]),'PRINT':([0,2,3,4,6,7,8,21,22,23,24,37,38,42,43,44,45,46,52,53,69,70,75,76,84,85,87,89,90,91,92,93,94,95,96,97,100,102,103,104,106,107,109,110,111,113,114,115,116,117,119,],[16,16,16,-5,-7,-8,-9,16,-4,16,-6,-26,-27,-18,-19,-20,-21,-22,16,-3,-29,-28,-2,16,16,16,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-49,16,-48,-51,-52,-30,-40,-41,16,16,-54,-50,-47,-53,]),'BREAK':([0,2,3,4,6,7,8,21,22,23,24,37,38,42,43,44,45,46,52,53,69,70,75,76,84,85,87,89,90,91,92,93,94,95,96,97,100,102,103,104,106,107,109,110,111,113,114,115,116,117,119,],[17,17,17,-5,-7,-8,-9,17,-4,17,-6,-26,-27,-18,-19,-20,-21,-22,17,-3,-29,-28,-2,17,17,17,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-49,17,-48,-51,-52,-30,-40,-41,17,17,-54,-50,-47,-53,]),'CONTINUE':([0,2,3,4,6,7,8,21,22,23,24,37,38,42,43,44,45,46,52,53,69,70,75,76,84,85,87,89,90,91,92,93,94,95,96,97,100,102,103,104,106,107,109,110,111,113,114,115,116,117,119,],[18,18,18,-5,-7,-8,-9,18,-4,18,-6,-26,-27,-18,-19,-20,-21,-22,18,-3,-29,-28,-2,18,18,18,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-49,18,-48,-51,-52,-30,-40,-41,18,18,-54,-50,-47,-53,]),'RETURN':([0,2,3,4,6,7,8,21,22,23,24,37,38,42,43,44,45,46,52,53,69,70,75,76,84,85,87,89,90,91,92,93,94,95,96,97,100,102,103,104,106,107,109,110,111,113,114,115,116,117,119,],[19,19,19,-5,-7,-8,-9,19,-4,19,-6,-26,-27,-18,-19,-20,-21,-22,19,-3,-29,-28,-2,19,19,19,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-49,19,-48,-51,-52,-30,-40,-41,19,19,-54,-50,-47,-53,]),'ID':([0,2,3,4,6,7,8,13,16,19,21,22,23,24,25,26,28,29,30,31,32,33,34,37,38,39,40,42,43,44,45,46,50,52,53,57,60,61,62,63,64,65,66,67,68,69,70,72,75,76,77,78,79,80,81,82,83,84,85,87,89,90,91,92,93,94,95,96,97,100,101,102,103,104,106,107,108,109,110,111,113,114,115,116,117,118,119,],[14,14,14,-5,-7,-8,-9,27,38,38,14,-4,14,-6,38,38,38,38,-55,-56,-57,-58,-59,-26,-27,38,38,-18,-19,-20,-21,-22,38,14,-3,38,38,38,38,38,38,38,38,38,38,-29,-28,38,-2,14,38,-60,-61,-62,-63,-64,-65,14,14,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,38,-49,14,-48,-51,-52,38,-30,-40,-41,14,14,-54,-50,-47,38,-53,]),'$end':([1,2,4,6,7,8,22,24,53,75,102,104,106,107,116,117,],[0,-1,-5,-7,-8,-9,-4,-6,-3,-2,-49,-48,-51,-52,-50,-47,]),'RBRACE':([4,6,7,8,22,23,24,52,53,75,102,104,106,107,114,116,117,],[-5,-7,-8,-9,-4,53,-6,75,-3,-2,-49,-48,-51,-52,117,-50,-47,]),'SEMICOLON':([5,9,10,17,18,35,36,37,38,42,43,44,45,46,51,59,69,70,73,74,87,88,89,90,91,92,93,94,95,96,97,100,109,110,111,112,],[24,-10,-11,-43,-44,-42,-17,-26,-27,-18,-19,-20,-21,-22,-45,-12,-29,-28,101,-25,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-30,-40,-41,-24,]),'ELSE':([6,7,8,24,102,104,106,107,116,117,],[-7,-8,-9,-6,113,-48,-51,-52,-50,-47,]),'LBRACKET':([11,12,16,19,25,26,28,29,30,31,32,33,34,39,40,41,47,48,49,50,57,60,61,62,63,64,65,66,67,68,72,77,78,79,80,81,82,83,101,108,118,],[25,26,40,40,40,40,40,40,-55,-56,-57,-58,-59,40,40,72,-66,-67,-68,40,40,40,40,40,40,40,40,40,40,40,40,40,-60,-61,-62,-63,-64,-65,40,40,40,]),'ASSIGN':([14,15,20,27,87,],[-13,30,-14,57,-15,]),'ADD_ASSIGN':([14,15,20,87,],[-13,31,-14,-15,]),'SUBSTRACT_ASSIGN':([14,15,20,87,],[-13,32,-14,-15,]),'MULTIPLY_ASSIGN':([14,15,20,87,],[-13,33,-14,-15,]),'DIVIDE_ASSIGN':([14,15,20,87,],[-13,34,-14,-15,]),'LSQUARE':([14,16,19,25,26,28,29,30,31,32,33,34,38,39,40,50,57,60,61,62,63,64,65,66,67,68,72,77,78,79,80,81,82,83,101,108,118,],[28,50,50,50,50,50,50,-55,-56,-57,-58,-59,28,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-60,-61,-62,-63,-64,-65,50,50,50,]),'MINUS':([16,19,25,26,28,29,30,31,32,33,34,36,37,38,39,40,42,43,44,45,46,50,51,55,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,77,78,79,80,81,82,83,86,87,88,89,90,91,92,93,94,95,96,97,98,100,101,105,108,109,110,111,115,118,119,],[39,39,39,39,39,39,-55,-56,-57,-58,-59,62,-26,-27,39,39,-18,-19,-20,-21,-22,39,62,62,39,62,39,39,39,39,39,39,39,39,39,-29,-28,62,39,39,-60,-61,-62,-63,-64,-65,62,-15,62,-32,-33,-34,-35,-36,-37,-38,-39,-31,62,-23,39,62,39,-30,-40,-41,62,39,62,]),'FLOAT':([16,19,25,26,28,29,30,31,32,33,34,39,40,50,57,60,61,62,63,64,65,66,67,68,72,77,78,79,80,81,82,83,101,108,118,],[42,42,42,42,42,42,-55,-56,-57,-58,-59,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-60,-61,-62,-63,-64,-65,42,42,42,]),'INT':([16,19,25,26,28,29,30,31,32,33,34,39,40,50,57,60,61,62,63,64,65,66,67,68,72,77,78,79,80,81,82,83,101,108,118,],[43,43,43,43,43,43,-55,-56,-57,-58,-59,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-60,-61,-62,-63,-64,-65,43,43,43,]),'STRING':([16,19,25,26,28,29,30,31,32,33,34,39,40,50,57,60,61,62,63,64,65,66,67,68,72,77,78,79,80,81,82,83,101,108,118,],[44,44,44,44,44,44,-55,-56,-57,-58,-59,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-60,-61,-62,-63,-64,-65,44,44,44,]),'EYE':([16,19,25,26,28,29,30,31,32,33,34,39,40,50,57,60,61,62,63,64,65,66,67,68,72,77,78,79,80,81,82,83,101,108,118,],[47,47,47,47,47,47,-55,-56,-57,-58,-59,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-60,-61,-62,-63,-64,-65,47,47,47,]),'ZEROS':([16,19,25,26,28,29,30,31,32,33,34,39,40,50,57,60,61,62,63,64,65,66,67,68,72,77,78,79,80,81,82,83,101,108,118,],[48,48,48,48,48,48,-55,-56,-57,-58,-59,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-60,-61,-62,-63,-64,-65,48,48,48,]),'ONES':([16,19,25,26,28,29,30,31,32,33,34,39,40,50,57,60,61,62,63,64,65,66,67,68,72,77,78,79,80,81,82,83,101,108,118,],[49,49,49,49,49,49,-55,-56,-57,-58,-59,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-60,-61,-62,-63,-64,-65,49,49,49,]),'COMMA':([35,36,37,38,42,43,44,45,46,58,69,70,74,87,88,89,90,91,92,93,94,95,96,97,98,99,100,109,110,111,112,],[60,-17,-26,-27,-18,-19,-20,-21,-22,60,-29,-28,60,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-31,-17,60,-23,-30,-40,-41,60,]),'RSQUARE':([36,37,38,42,43,44,45,46,58,69,70,73,74,87,88,89,90,91,92,93,94,95,96,97,100,109,110,111,112,],[-17,-26,-27,-18,-19,-20,-21,-22,87,-29,-28,100,-25,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-30,-40,-41,-24,]),'PLUS':([36,37,38,42,43,44,45,46,51,55,59,69,70,71,86,87,88,89,90,91,92,93,94,95,96,97,98,100,105,109,110,111,115,119,],[61,-26,-27,-18,-19,-20,-21,-22,61,61,61,-29,-28,61,61,-15,61,-32,-33,-34,-35,-36,-37,-38,-39,-31,61,-23,61,-30,-40,-41,61,61,]),'TIMES':([36,37,38,42,43,44,45,46,51,55,59,69,70,71,86,87,88,89,90,91,92,93,94,95,96,97,98,100,105,109,110,111,115,119,],[63,-26,-27,-18,-19,-20,-21,-22,63,63,63,-29,-28,63,63,-15,63,63,63,-34,-35,63,63,-38,-39,-31,63,-23,63,-30,-40,-41,63,63,]),'DIVIDE':([36,37,38,42,43,44,45,46,51,55,59,69,70,71,86,87,88,89,90,91,92,93,94,95,96,97,98,100,105,109,110,111,115,119,],[64,-26,-27,-18,-19,-20,-21,-22,64,64,64,-29,-28,64,64,-15,64,64,64,-34,-35,64,64,-38,-39,-31,64,-23,64,-30,-40,-41,64,64,]),'MPLUS':([36,37,38,42,43,44,45,46,51,55,59,69,70,71,86,87,88,89,90,91,92,93,94,95,96,97,98,100,105,109,110,111,115,119,],[65,-26,-27,-18,-19,-20,-21,-22,65,65,65,-29,-28,65,65,-15,65,-32,-33,-34,-35,-36,-37,-38,-39,-31,65,-23,65,-30,-40,-41,65,65,]),'MMINUS':([36,37,38,42,43,44,45,46,51,55,59,69,70,71,86,87,88,89,90,91,92,93,94,95,96,97,98,100,105,109,110,111,115,119,],[66,-26,-27,-18,-19,-20,-21,-22,66,66,66,-29,-28,66,66,-15,66,-32,-33,-34,-35,-36,-37,-38,-39,-31,66,-23,66,-30,-40,-41,66,66,]),'MTIMES':([36,37,38,42,43,44,45,46,51,55,59,69,70,71,86,87,88,89,90,91,92,93,94,95,96,97,98,100,105,109,110,111,115,119,],[67,-26,-27,-18,-19,-20,-21,-22,67,67,67,-29,-28,67,67,-15,67,67,67,-34,-35,67,67,-38,-39,-31,67,-23,67,-30,-40,-41,67,67,]),'MDIVIDE':([36,37,38,42,43,44,45,46,51,55,59,69,70,71,86,87,88,89,90,91,92,93,94,95,96,97,98,100,105,109,110,111,115,119,],[68,-26,-27,-18,-19,-20,-21,-22,68,68,68,-29,-28,68,68,-15,68,68,68,-34,-35,68,68,-38,-39,-31,68,-23,68,-30,-40,-41,68,68,]),'LESSER':([37,38,42,43,44,45,46,55,69,70,87,89,90,91,92,93,94,95,96,97,100,109,110,111,],[-26,-27,-18,-19,-20,-21,-22,78,-29,-28,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-30,-40,-41,]),'GREATER':([37,38,42,43,44,45,46,55,69,70,87,89,90,91,92,93,94,95,96,97,100,109,110,111,],[-26,-27,-18,-19,-20,-21,-22,79,-29,-28,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-30,-40,-41,]),'EQUALS':([37,38,42,43,44,45,46,55,69,70,87,89,90,91,92,93,94,95,96,97,100,109,110,111,],[-26,-27,-18,-19,-20,-21,-22,80,-29,-28,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-30,-40,-41,]),'NOT_EQUALS':([37,38,42,43,44,45,46,55,69,70,87,89,90,91,92,93,94,95,96,97,100,109,110,111,],[-26,-27,-18,-19,-20,-21,-22,81,-29,-28,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-30,-40,-41,]),'LESSER_EQUALS':([37,38,42,43,44,45,46,55,69,70,87,89,90,91,92,93,94,95,96,97,100,109,110,111,],[-26,-27,-18,-19,-20,-21,-22,82,-29,-28,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-30,-40,-41,]),'GREATER_EQUALS':([37,38,42,43,44,45,46,55,69,70,87,89,90,91,92,93,94,95,96,97,100,109,110,111,],[-26,-27,-18,-19,-20,-21,-22,83,-29,-28,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-30,-40,-41,]),'RBRACKET':([37,38,42,43,44,45,46,54,56,69,70,71,87,88,89,90,91,92,93,94,95,96,97,98,99,100,105,109,110,111,],[-26,-27,-18,-19,-20,-21,-22,76,84,-29,-28,97,-15,-16,-32,-33,-34,-35,-36,-37,-38,-39,-31,110,111,-23,-46,-30,-40,-41,]),'RANGE':([37,38,42,43,44,45,46,69,70,86,87,89,90,91,92,93,94,95,96,97,100,109,110,111,115,],[-26,-27,-18,-19,-20,-21,-22,-29,-28,108,-15,-32,-33,-34,-35,-36,-37,-38,-39,-31,-23,-30,-40,-41,118,]),'TRANSPOSITION':([38,97,],[69,109,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'CODE_BLOCK':([0,3,21,103,],[2,23,52,114,]),'instruction':([0,2,3,21,23,52,76,84,85,103,113,114,],[4,22,4,4,22,22,104,104,104,4,104,22,]),'statement':([0,2,3,21,23,52,76,84,85,103,113,114,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'if_statement':([0,2,3,21,23,52,76,84,85,103,113,114,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'while_statement':([0,2,3,21,23,52,76,84,85,103,113,114,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'for_statement':([0,2,3,21,23,52,76,84,85,103,113,114,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'assignment':([0,2,3,21,23,52,76,84,85,103,113,114,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'keyword':([0,2,3,21,23,52,76,84,85,103,113,114,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'variable':([0,2,3,21,23,52,76,84,85,103,113,114,],[15,15,15,15,15,15,15,15,15,15,15,15,]),'variable_attribute':([0,2,3,16,19,21,23,25,26,28,29,39,40,50,52,57,60,61,62,63,64,65,66,67,68,72,76,77,84,85,101,103,108,113,114,118,],[20,20,20,46,46,20,20,46,46,46,46,46,46,46,20,46,46,46,46,46,46,46,46,46,46,46,20,46,20,20,46,20,46,20,20,46,]),'assignment_operator':([15,],[29,]),'sequence':([16,28,50,72,101,],[35,58,74,99,112,]),'expression':([16,19,25,26,28,29,39,40,50,57,60,61,62,63,64,65,66,67,68,72,77,101,108,118,],[36,51,55,55,36,59,70,71,36,86,88,89,90,91,92,93,94,95,96,98,105,36,115,119,]),'value':([16,19,25,26,28,29,39,40,50,57,60,61,62,63,64,65,66,67,68,72,77,101,108,118,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'function':([16,19,25,26,28,29,39,40,50,57,60,61,62,63,64,65,66,67,68,72,77,101,108,118,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'matrix':([16,19,25,26,28,29,39,40,50,57,60,61,62,63,64,65,66,67,68,72,77,101,108,118,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'relation':([25,26,],[54,56,]),'rows':([50,],[73,]),'logic_operator':([55,],[77,]),'range':([57,],[85,]),'body':([76,84,85,113,],[102,106,107,116,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('PROGRAM -> CODE_BLOCK','PROGRAM',1,'p_program','Mparser.py',29),
  ('CODE_BLOCK -> CODE_BLOCK LBRACE CODE_BLOCK RBRACE','CODE_BLOCK',4,'p_code_block_braces','Mparser.py',34),
  ('CODE_BLOCK -> LBRACE CODE_BLOCK RBRACE','CODE_BLOCK',3,'p_code_block_braces','Mparser.py',35),
  ('CODE_BLOCK -> CODE_BLOCK instruction','CODE_BLOCK',2,'p_code_block','Mparser.py',45),
  ('CODE_BLOCK -> instruction','CODE_BLOCK',1,'p_code_block','Mparser.py',46),
  ('instruction -> statement SEMICOLON','instruction',2,'p_instruction','Mparser.py',56),
  ('instruction -> if_statement','instruction',1,'p_instruction','Mparser.py',57),
  ('instruction -> while_statement','instruction',1,'p_instruction','Mparser.py',58),
  ('instruction -> for_statement','instruction',1,'p_instruction','Mparser.py',59),
  ('statement -> assignment','statement',1,'p_statement','Mparser.py',65),
  ('statement -> keyword','statement',1,'p_statement','Mparser.py',66),
  ('assignment -> variable assignment_operator expression','assignment',3,'p_assignment','Mparser.py',72),
  ('variable -> ID','variable',1,'p_variable','Mparser.py',78),
  ('variable -> variable_attribute','variable',1,'p_variable','Mparser.py',79),
  ('variable_attribute -> ID LSQUARE sequence RSQUARE','variable_attribute',4,'p_variable_attribute','Mparser.py',85),
  ('sequence -> sequence COMMA expression','sequence',3,'p_sequence','Mparser.py',91),
  ('sequence -> expression','sequence',1,'p_sequence','Mparser.py',92),
  ('value -> FLOAT','value',1,'p_value','Mparser.py',102),
  ('value -> INT','value',1,'p_value','Mparser.py',103),
  ('value -> STRING','value',1,'p_value','Mparser.py',104),
  ('value -> matrix','value',1,'p_value','Mparser.py',105),
  ('value -> variable_attribute','value',1,'p_value','Mparser.py',106),
  ('matrix -> LSQUARE rows RSQUARE','matrix',3,'p_matrix','Mparser.py',113),
  ('rows -> rows SEMICOLON sequence','rows',3,'p_rows','Mparser.py',119),
  ('rows -> sequence','rows',1,'p_rows','Mparser.py',120),
  ('expression -> value','expression',1,'p_expression_value','Mparser.py',130),
  ('expression -> ID','expression',1,'p_expression_id','Mparser.py',135),
  ('expression -> MINUS expression','expression',2,'p_expression_negation','Mparser.py',140),
  ('expression -> ID TRANSPOSITION','expression',2,'p_id_transposition','Mparser.py',146),
  ('expression -> LBRACKET expression RBRACKET TRANSPOSITION','expression',4,'p_expression_transposition','Mparser.py',152),
  ('expression -> LBRACKET expression RBRACKET','expression',3,'p_expression_bracket','Mparser.py',158),
  ('expression -> expression PLUS expression','expression',3,'p_bin_expressions','Mparser.py',164),
  ('expression -> expression MINUS expression','expression',3,'p_bin_expressions','Mparser.py',165),
  ('expression -> expression TIMES expression','expression',3,'p_bin_expressions','Mparser.py',166),
  ('expression -> expression DIVIDE expression','expression',3,'p_bin_expressions','Mparser.py',167),
  ('expression -> expression MPLUS expression','expression',3,'p_bin_expressions','Mparser.py',168),
  ('expression -> expression MMINUS expression','expression',3,'p_bin_expressions','Mparser.py',169),
  ('expression -> expression MTIMES expression','expression',3,'p_bin_expressions','Mparser.py',170),
  ('expression -> expression MDIVIDE expression','expression',3,'p_bin_expressions','Mparser.py',171),
  ('expression -> function LBRACKET expression RBRACKET','expression',4,'p_expression_fun','Mparser.py',177),
  ('expression -> function LBRACKET sequence RBRACKET','expression',4,'p_expression_fun','Mparser.py',178),
  ('keyword -> PRINT sequence','keyword',2,'p_keyword_print','Mparser.py',184),
  ('keyword -> BREAK','keyword',1,'p_keyword_break','Mparser.py',190),
  ('keyword -> CONTINUE','keyword',1,'p_keyword_continue','Mparser.py',196),
  ('keyword -> RETURN expression','keyword',2,'p_keyword_return','Mparser.py',202),
  ('relation -> expression logic_operator expression','relation',3,'p_relation','Mparser.py',207),
  ('body -> LBRACE CODE_BLOCK RBRACE','body',3,'p_body','Mparser.py',211),
  ('body -> instruction','body',1,'p_body','Mparser.py',212),
  ('if_statement -> IF LBRACKET relation RBRACKET body','if_statement',5,'p_if_statement','Mparser.py',220),
  ('if_statement -> IF LBRACKET relation RBRACKET body ELSE body','if_statement',7,'p_if_else_statement','Mparser.py',226),
  ('while_statement -> WHILE LBRACKET relation RBRACKET body','while_statement',5,'p_while_statement','Mparser.py',231),
  ('for_statement -> FOR ID ASSIGN range body','for_statement',5,'p_for_statement','Mparser.py',235),
  ('range -> expression RANGE expression RANGE expression','range',5,'p_range','Mparser.py',239),
  ('range -> expression RANGE expression','range',3,'p_range','Mparser.py',240),
  ('assignment_operator -> ASSIGN','assignment_operator',1,'p_assignment_operator','Mparser.py',248),
  ('assignment_operator -> ADD_ASSIGN','assignment_operator',1,'p_assignment_operator','Mparser.py',249),
  ('assignment_operator -> SUBSTRACT_ASSIGN','assignment_operator',1,'p_assignment_operator','Mparser.py',250),
  ('assignment_operator -> MULTIPLY_ASSIGN','assignment_operator',1,'p_assignment_operator','Mparser.py',251),
  ('assignment_operator -> DIVIDE_ASSIGN','assignment_operator',1,'p_assignment_operator','Mparser.py',252),
  ('logic_operator -> LESSER','logic_operator',1,'p_comparision_operator','Mparser.py',258),
  ('logic_operator -> GREATER','logic_operator',1,'p_comparision_operator','Mparser.py',259),
  ('logic_operator -> EQUALS','logic_operator',1,'p_comparision_operator','Mparser.py',260),
  ('logic_operator -> NOT_EQUALS','logic_operator',1,'p_comparision_operator','Mparser.py',261),
  ('logic_operator -> LESSER_EQUALS','logic_operator',1,'p_comparision_operator','Mparser.py',262),
  ('logic_operator -> GREATER_EQUALS','logic_operator',1,'p_comparision_operator','Mparser.py',263),
  ('function -> EYE','function',1,'p_function','Mparser.py',269),
  ('function -> ZEROS','function',1,'p_function','Mparser.py',270),
  ('function -> ONES','function',1,'p_function','Mparser.py',271),
]
