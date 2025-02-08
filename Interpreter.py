import sys

from time import perf_counter

from Environment import Environment
from CustomException import CustomException

from operations.Cmp import Cmp
from operations.Mov import Mov
from operations.Add import Add
from operations.Sub import Sub
from operations.Mul import Mul
from operations.Mod import Mod
from operations.Printf import Printf

from operations.Exit import Exit
from operations.B import B
from operations.Bgt import Bgt
from operations.Bge import Bge
from operations.Ble import Ble
from operations.Blt import Blt
from operations.Beq import Beq
from operations.Bne import Bne


class Interpreter:

    def __init__(self, file_name):
        self.DEBUG = False # if we want to debug Interpreter.run()
        self.environment = Environment()
        self.commands = []

        try:
            with open(file_name) as code:
                line = 0
                commands = code.readlines()
                for command in commands:
                    line += 1
                    command = command.strip()

                    if not command or command.startswith("//"):
                        self.commands.append(None)
                        continue

                    command = command.split()
                    
                    if command[0].endswith(":"):
                        self.environment.add_label(command[0][:-1], line)
                        if len(command) > 1:
                            command = command[1:]
                        else:
                            self.commands.append(None)
                            continue

                    self.commands.append(command)
                
        except FileNotFoundError:
            print(f"File \"{file_name}\" not found!")
            sys.exit()

    def run(self):
        t1 = perf_counter()
        while self.environment.counter <= len(self.commands) and self.environment.counter >= 0:
            command = self.commands[self.environment.counter-1]
            self.environment.counter += 1
            if command == None:
                continue
            if not self.DEBUG:
                try:
                    self.execute(command)
                except:
                    print(f"Error at line {self.environment.counter}")
                    sys.exit()
            else:
                self.execute(command)
        
        if self.environment.counter == -1:
            print(f"program ended succesfully in {perf_counter() - t1} seconds")
        else:
            print("Program did not exit correctly")
        sys.exit()
    
    def execute(self, command):
        operation = command[0]

        if operation == "exit":
            Exit.execute(self.environment, command)

        elif operation == "b":
            B.execute(self.environment, command)

        elif operation == "b.eq":
            Beq.execute(self.environment, command)
        
        elif operation == "b.ne":
            Bne.execute(self.environment, command)

        elif operation == "b.gt":
            Bgt.execute(self.environment, command)
        
        elif operation == "b.ge":
            Bge.execute(self.environment, command)

        elif operation == "b.le":
            Ble.execute(self.environment, command)

        elif operation == "b.lt":
            Blt.execute(self.environment, command)

        elif operation == "cmp":
            Cmp.execute(self.environment, command)

        elif operation == "mov":
            Mov.execute(self.environment, command)

        elif operation == "add":
            Add.execute(self.environment, command)

        elif operation == "sub":
            Sub.execute(self.environment, command)

        elif operation == "mul":
            Mul.execute(self.environment, command)

        elif operation == "mod":
            Mod.execute(self.environment, command)

        elif operation == "printf":
            Printf.execute(self.environment, command)

        else:
            print(f"Unknown operation \"{operation}\"")
            raise CustomException