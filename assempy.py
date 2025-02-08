import sys

from Interpreter import Interpreter

def main(file_name):

    interpreter = Interpreter(file_name)

    interpreter.run()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        file_name = input("Enter a file to execute: ")
    elif len(sys.argv) > 2:
        print("too many parameters")
        file_name = False
    else:
        file_name = sys.argv[1]

    if file_name:
        main(file_name)
