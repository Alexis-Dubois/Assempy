from .Operation import Operation

class Blt(Operation):
    args_needed = 1
    operation_code = "blt"

    @staticmethod
    def execute(environment, args):
        Blt.count_args(Blt, len(args)-1)

        if environment.flags["C"] == 0 and environment.flags["Z"] == 0:
            Blt.branch_to(environment, args[1])