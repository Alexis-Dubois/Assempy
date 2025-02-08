from .Operation import Operation

class Beq(Operation):
    args_needed = 1
    operation_code = "beq"

    @staticmethod
    def execute(environment, args):
        Beq.count_args(Beq, len(args)-1)

        if environment.flags["Z"] == 1:
            Beq.branch_to(environment, args[1])