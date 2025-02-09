from .Operation import Operation

class udiv(Operation):
    args_needed = 3
    operation_code = "udiv"

    @staticmethod
    def execute(environment, args):
        udiv.count_args(udiv, len(args)-1)

        destination = args[1]
        value1 = environment.decode_argument(args[2])
        value2 = environment.decode_argument(args[3])

        environment.set_registre_value(destination, value1/value2)