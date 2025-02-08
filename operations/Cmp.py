from .Operation import Operation

class Cmp(Operation):
    args_needed = 2
    operation_code = "cmp"

    @staticmethod
    def execute(environment, args):
        Cmp.count_args(Cmp, len(args)-1)

        environment.update_flag(args[1], args[2])