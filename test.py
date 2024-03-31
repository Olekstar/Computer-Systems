from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def main():
    test_cases = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "10 / 2",
        "5 * (10 - 3)",
        "100 - 4 * 3 / 2"
    ]
    
    for expression in test_cases:
        lexer = Lexer(expression)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        print(f"Результат виразу '{expression}': {result}")

if __name__ == "__main__":
    main()
