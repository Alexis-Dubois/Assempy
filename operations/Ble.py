from .Operation import Operation

class Ble(Operation):
    args_needed = 1
    operation_code = "ble"

    @staticmethod
    def execute(environment, args):
        Ble.count_args(Ble, len(args)-1)

        if environment.flags["C"] == 0:
            Ble.branch_to(environment, args[1])