from src.lexer import BasicLexer
from src.parser import BasicParser
from src.interpreter import BasicExecute
from sys import *


def open_file(filename):
    data = open(filename, "r").read()
    return data


if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    #interpreter = basicinterpreter
    env = {}
    if len(argv) > 1:
        data = open(argv[1])
        text = data.readlines()
        for line in text:
            #lex = lexer.tokenize(line)
            tree = parser.parse(lexer.tokenize(line))
            BasicExecute(tree, env)
    else:
        while True:
            try:
                text = input('liyn_language » ')
            except EOFError:
                break
            if text:
                tree = parser.parse(lexer.tokenize(text))
                BasicExecute(tree, env)
