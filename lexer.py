import constant
from token import Token
class Lexer:
    def __init__(self):
        self.tokens = []
        pass
    
    def appendToken(self,word, type):
        if(len(word)>0):
            word = word.rstrip()
            word = word.lstrip()
            self.tokens.append(Token(type,word))
        pass
            
    def discriminateDigitandID(self,word):
        if(word.isdigit()):
            self.appendToken(word,"NUMBER")
        else:
            self.appendToken(word,"ID")
        pass


    def getTokens(self):
        return self.tokens
    def lex(self,f):
        content = f.read()
        word = ""
        quotes_count = 0
        for i in content:
            if(i not in constant.operators and i !='\n'):
                word+=i
            if(i=='"'):
                quotes_count+=1
            if(i=="\n"):
                self.discriminateDigitandID(word)
                word = ""
                quotes_count = 0
                continue
            if(quotes_count==2):
                self.appendToken(word,"STRING")
                quotes_count = 0
                word = ""
                continue
            if(quotes_count == 0):
                if(i in constant.operators):
                    self.discriminateDigitandID(word)
                    self.appendToken(i,constant.operators.get(i))
                    word = ""
                if(word.strip() in constant.keywords):
                    self.appendToken(word,constant.keywords.get(word))
                    word = ""
            return self.tokens
