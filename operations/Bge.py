from .Operation import Operation

class Bge(Operation):
    args_needed = 1
    operation_code = "bge"

    @staticmethod
    def execute(environment, args):
        Bge.count_args(Bge, len(args)-1)

        if environment.flags["C"] == 1:
            Bge.branch_to(environment, args[1])