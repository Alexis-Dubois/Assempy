from .Operation import Operation

class Msub(Operation):
    args_needed = 4
    operation_code = "msub"

    @staticmethod
    def execute(environment, args):
        madd.count_args(Msub, len(args)-1)

        destination = args[1]
        value1 = environment.decode_argument(args[2])
        value2 = environment.decode_argument(args[3])
        value3 = environment.decode_argument(args[4])

        environment.set_registre_value(destination, (value1*value2) - value3)