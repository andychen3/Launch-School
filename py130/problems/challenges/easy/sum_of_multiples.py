# https://launchschool.com/exercises/47a18b59

"""
input: number, and a set of one or more other numbers.
output: find the sum of all multiples of the numbers in the set that are less than
the first number. if the set of numbers is not given default to 3 and 5.
rules:

DS:

Algo:


# """
class SumOfMultiples:

    def __init__(self, *args):
        self.multiples = args

    @classmethod
    def sum_up_to(cls, number, *args):
        """
        Uses the default set of 3 and 5
        """
        multiples = [3, 5] if not args else args
        
        _sum = 0

        for num in range(number):
            for multiple in multiples:
                if num % multiple == 0:
                    _sum += num
                    break
        return _sum


    def to(self, number):
        return self.sum_up_to(number, *self.multiples)



