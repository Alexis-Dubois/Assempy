from .Operation import Operation

class Add(Operation):
    args_needed = 3
    operation_code = "add"

    @staticmethod
    def execute(environment, args):
        Add.count_args(Add, len(args)-1)

        destination = args[1]
        value1 = environment.decode_argument(args[2])
        value2 = environment.decode_argument(args[3])

        environment.set_registre_value(destination, value1+value2)