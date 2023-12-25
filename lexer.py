import constant
from token import Token
class Lexer:
    def __init__(self) -> None:
        self.tokens = []
        pass
    
    def appendToken(self,word, type):
            if(len(word)>0):
                word = word.rstrip()
                word = word.lstrip()
                self.tokens.append(Token(type,word))
    def getTokens(self):
        return self.tokens
    def lex(self,f):
        content = f.read()
        word = ""
        cnt = 0
        for i in content:
            if(i not in constant.operators and i !='\n'):
                word+=i
            if(i=='"'):
                cnt+=1
            if(i=="\n"):
                if(word.strip().isdigit()):
                    self.appendToken(word,"NUMBER")
                else:
                    self.appendToken(word,"ID")
                word = ""
                cnt = 0
                continue
            if(cnt==2):
                self.appendToken(word,"STRING")
                cnt = 0
                word = ""
                continue
            if(cnt == 0):
                if(i in constant.operators):
                    if(word.isdigit()):
                        self.appendToken(word,"NUMBER")
                    else:
                        self.appendToken(word,"ID")
                    
                    self.appendToken(i,constant.operators.get(i))
                    word = ""
                if(word.strip() in constant.keywords):
                    self.appendToken(word,constant.keywords.get(word))
                    word = ""
            return self.tokens
