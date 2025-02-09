from .Operation import Operation

class And(Operation):
    args_needed = 3
    operation_code = "and"

    @staticmethod
    def execute(environment, args):
        Add.count_args(And, len(args)-1)

        destination = args[1]
        value1 = environment.decode_argument(args[2])
        value2 = environment.decode_argument(args[3])
        binary_value1 = bin(args[2])
        binary_value2 = bin(args[3])
        environment.set_registre_value(destination, binary_value1 and binary_value2)