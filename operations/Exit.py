from .Operation import Operation

class Exit(Operation):
    args_needed = 0
    operation_code = "exit"

    @staticmethod
    def execute(environment, args):
        Exit.count_args(Exit, len(args)-1)

        Exit.branch_to(environment, "#-1")