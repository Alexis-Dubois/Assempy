from .Operation import Operation

class B(Operation):
    args_needed = 1
    operation_code = "b"

    @staticmethod
    def execute(environment, args):
        B.count_args(B, len(args)-1)

        B.branch_to(environment, args[1])