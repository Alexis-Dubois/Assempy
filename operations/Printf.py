from .Operation import Operation

class Printf(Operation):
    args_needed = 0
    operation_code = "printf"

    @staticmethod
    def execute(environment, args):
        Printf.count_args(Printf, len(args)-1)

        print(environment.get_registre_value("x0"))