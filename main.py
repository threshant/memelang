from tok import *
from lexer import *
f = open("lang.txt","r")
lexer = Lexer()
lexer.lex(f)
for i in lexer.getTokens():
    print(i.content,":",i.method)