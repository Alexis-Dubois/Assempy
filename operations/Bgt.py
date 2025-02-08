from .Operation import Operation

class Bgt(Operation):
    args_needed = 1
    operation_code = "bgt"

    @staticmethod
    def execute(environment, args):
        Bgt.count_args(Bgt, len(args)-1)

        if environment.flags["Z"] == 0 and environment.flags["C"] == 1:
            Bgt.branch_to(environment, args[1])