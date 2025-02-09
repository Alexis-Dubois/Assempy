from .Operation import Operation

class Madd(Operation):
    args_needed = 4
    operation_code = "madd"

    @staticmethod
    def execute(environment, args):
        Madd.count_args(Madd, len(args)-1)

        destination = args[1]
        value1 = environment.decode_argument(args[2])
        value2 = environment.decode_argument(args[3])
        value3 = environment.decode_argument(args[4])

        environment.set_registre_value(destination, (value1*value2) + value3)