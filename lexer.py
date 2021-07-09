#######################################
# IMPORTS
#######################################

from sly import Lexer


class BasicLexer(Lexer):
    tokens = {NAME, NUMBER, STRING, IF, THEN,
              ELSE, FOR, FUN, TO, ARROW, EQEQ, PRINT}
    ignore = '\t '

    literals = {'=', '+', '-', '/', '*', '(', ')', ',', ';'}

    # Mendefinisikan token
    IF = r'MENAWI'
    THEN = r'DADOS'
    ELSE = r'LIYANE'
    FOR = r'KAGEM'
    FUN = r'FUNGSI'
    TO = r'ING'
    PRINT = r'NYITHAK'
    ARROW = r'->'
    NAME = r'[A-Za-z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')
    
     
    def error (self, t) :
        print ("illegal character '%s'" % t.value[0])
        self.index += 1
        
    if __name__ == '__main__':
        lexer = BasicLexer()
        env   = {}
        while True:
            try:
                text = input('basic > ')
            except EOFError:
                break
            if text:
                lex = lexer.tokenize(text)
                for token in lex:
                    print(token)
    
