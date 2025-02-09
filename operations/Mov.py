from .Operation import Operation

class Mov(Operation):
    args_needed = 2
    operation_code = "mov"

    @staticmethod
    def execute(environment, args):
        Mov.count_args(Mov, len(args)-1)

        destination = args[1]
        value = environment.decode_argument(args[2])

        environment.set_registre_value(destination, value)