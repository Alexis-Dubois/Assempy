from CustomException import CustomException

from collections import defaultdict

class Environment:

    def __init__(self):
        MEMORY_SIZE = 2**16
        self.registres = dict()

        for i in range(31):
            self.registres["x"+str(i)] = 0

        self.memory = [[0] for i in range(MEMORY_SIZE)]

        self.labels = defaultdict(lambda: -1)

        self.flags = {"Z":0, "N":0, "C":0, "V":0}

    def get_registre_value(self, registre):
        self._check_valid_registre(registre)
        return self.registres[registre]
    
    def set_registre_value(self, registre, value):
        self._check_valid_registre(registre)
        self.registres[registre] = value
    
    def get_memory_value(self, pos):
        return self.memory[pos]
    
    def set_memory_value(self, pos, value):
        self.memory[pos] = value

    def _check_valid_registre(self, registre):
        if registre not in self.registres:
            print(f"registre \"{registre}\" unknown")
            raise CustomException
        
    def decode_argument(self, value):
        if value.startswith("#"):
            value = int(value[1:])
        else:
            value = self.get_registre_value(value)
        return value
    
    def decode_label(self, label):
        return self.labels[label]
    
    def update_flag(self, a, b):
        a = self.decode_argument(a)
        b = self.decode_argument(b)

        if a == b:
            self.flags["Z"] = 1
        else:
            self.flags["Z"] = 0

        if a > b or self.flags["Z"]:
            self.flags["C"] = 1
        else:
            self.flags["C"] = 0
    
    def add_label(self, label, line):
        self.labels[label] = line

