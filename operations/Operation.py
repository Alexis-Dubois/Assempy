from abc import ABC, abstractmethod

from CustomException import CustomException

class Operation(ABC):
    args_needed = None # Abstract
    operation_code = None # Abstract

    @staticmethod
    def count_args(cls, args_received):
        if args_received != cls.args_needed:
            print(f"Operation {cls.operation_code} take {cls.args_needed} arguments, received {args_received}")
            raise CustomException

    def branch_to(environment, destination):
        value = environment.decode_label(destination)

        if value == -1: # it was not a label
            value = environment.decode_argument(destination)

        environment.counter = value

    @abstractmethod
    def execute():
        pass