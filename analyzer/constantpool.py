from .constant import Constant

class ConstantPool:
    pool = {}

    def __init__(self, count, data):
        """Creates a constant pool from the data"""

        self.cpcount = count
        self.data = data

        constants = count - 1

        index = 1

        while index <= constants:
            derp = Constant(data, index)
            data = self.data = derp.data # Set data to trimmed data

            self.pool[index] = derp

            index += 1

            if derp.type == Constant.DOUBLE or derp.type == Constant.LONG:
                index += 1

        # Solve references after pool has been generated
        for const in self.pool.items():
            const[1]._solve_ref(self.pool)

    def get_constants(self):
        return self.pool

    def get_data(self):
        return self.data # return the trimmed data (without the constant pool)

    def __getitem__(self, item):
        return self.pool[item]

