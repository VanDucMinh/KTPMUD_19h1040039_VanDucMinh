import math

class Real_Number:
    def __init__(self, real_number):
        self.real_number = real_number

    def module(self):
        return abs(self.real_number)


class Complex_Number(Real_Number):
    def __init__(self, real_number, image_number):
        super().__init__(real_number)
        self.image_number = image_number

    def module(self):
        return math.sqrt((self.real_number * 2) + (self.image_number * 2))


num = Complex_Number(10, 3)
print(num.module())