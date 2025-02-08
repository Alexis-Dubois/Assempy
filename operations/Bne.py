from .Operation import Operation

class Bne(Operation):
    args_needed = 1
    operation_code = "bne"

    @staticmethod
    def execute(environment, args):
        Bne.count_args(Bne, len(args)-1)

        if environment.flags["Z"] == 0:
            Bne.branch_to(environment, args[1])