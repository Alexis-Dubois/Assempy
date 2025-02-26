from .Operation import Operation

class Mul(Operation):
    args_needed = 3
    operation_code = "mul"

    @staticmethod
    def execute(environment, args):
        Mul.count_args(Mul, len(args)-1)

        destination = args[1]
        value1 = environment.decode_argument(args[2])
        value2 = environment.decode_argument(args[3])

        environment.set_registre_value(destination, value1*value2)