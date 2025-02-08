import sys

from time import perf_counter

from Environment import Environment
from CustomException import CustomException

class Interpreter:

    def __init__(self, file_name):
        self.DEBUG = False # if we want to debug Interpreter.run()
        self.environment = Environment()
        self.commands = []
        self.counter = 1

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
        while self.counter <= len(self.commands) and self.counter >= 0:
            command = self.commands[self.counter-1]
            self.counter += 1
            if command == None:
                continue
            if not self.DEBUG:
                try:
                    self.execute(command)
                except:
                    print(f"Error at line {self.counter}")
                    sys.exit()
            else:
                self.execute(command)
        
        if self.counter == -1:
            print(f"program ended succesfully in {perf_counter() - t1} seconds")
        else:
            print("Program did not exit correctly")
        sys.exit()
    
    def execute(self, command):
        operation = command[0]

        if operation == "exit":
            self.counter = -1

        elif operation == "cmp":
            if len(command) != 3:
                print(f"Operation cmp take 2 arguments, received {len(command)-1}")
                raise CustomException
            
            self.environment.update_flag(command[1], command[2])

        elif operation == "b":
            if len(command) != 2:
                print(f"Operation branch take 1 arguments, received {len(command)-1}")
                raise CustomException
            self.branch_to(command[1])

        elif operation == "b.eq":
            if len(command) != 2:
                print(f"Operation branch take 1 arguments, received {len(command)-1}")
                raise CustomException
            if self.environment.flags["Z"] == 1:
                self.branch_to(command[1])
        
        elif operation == "b.ne":
            if len(command) != 2:
                print(f"Operation branch take 1 arguments, received {len(command)-1}")
                raise CustomException
            if self.environment.flags["Z"] == 0:
                self.branch_to(command[1])

        elif operation == "b.gt":
            if len(command) != 2:
                print(f"Operation branch take 1 arguments, received {len(command)-1}")
                raise CustomException
            if self.environment.flags["Z"] == 0 and self.environment.flags["C"] == 1:
                self.branch_to(command[1])
        
        elif operation == "b.ge":
            if len(command) != 2:
                print(f"Operation branch take 1 arguments, received {len(command)-1}")
                raise CustomException
            if self.environment.flags["C"] == 1:
                self.branch_to(command[1])

        elif operation == "b.le":
            if len(command) != 2:
                print(f"Operation branch take 1 arguments, received {len(command)-1}")
                raise CustomException
            if self.environment.flags["C"] == 0:
                self.branch_to(command[1])

        elif operation == "b.lt":
            if len(command) != 2:
                print(f"Operation branch take 1 arguments, received {len(command)-1}")
                raise CustomException
            if self.environment.flags["C"] == 0 and self.environment.flags["Z"] == 0:
                self.branch_to(command[1])

        elif operation == "mov":
            if len(command) != 3:
                print(f"Operation mov take 2 arguments, received {len(command)-1}")
                raise CustomException
            
            destination = command[1]
            value = self.environment.decode_argument(command[2])

            self.environment.set_registre_value(destination, value)

        elif operation == "add":
            if len(command) != 4:
                print(f"Operation add take 3 arguments, received {len(command)-1}")
                raise CustomException
            
            destination = command[1]

            value1 = self.environment.decode_argument(command[2])
            value2 = self.environment.decode_argument(command[3])
            
            self.environment.set_registre_value(destination, value1+value2)

        elif operation == "mul":
            if len(command) != 4:
                print(f"Operation add take 3 arguments, received {len(command)-1}")
                raise CustomException
            
            destination = command[1]

            value1 = self.environment.decode_argument(command[2])
            value2 = self.environment.decode_argument(command[3])
            
            self.environment.set_registre_value(destination, value1*value2)

        elif operation == "mod":
            if len(command) != 4:
                print(f"Operation add take 3 arguments, received {len(command)-1}")
                raise CustomException
            
            destination = command[1]

            value1 = self.environment.decode_argument(command[2])
            value2 = self.environment.decode_argument(command[3])
            
            self.environment.set_registre_value(destination, value1%value2)

        elif operation == "printf":
            print(self.environment.get_registre_value("x0"))

        else:
            print(f"Unknown operation \"{operation}\"")
            raise CustomException
        

    def branch_to(self, destination):
        value = self.environment.decode_label(destination)

        if value == -1: # it was not a label
            value = self.environment.decode_argument(destination)

        self.counter = value



