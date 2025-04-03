# https://launchschool.com/exercises/376a5755

"""
input: a number
output: returns if perfect, abundant, or deficient
rules:
1. Sum of all positive divisors that are evenly divided
2. Perfect numbers have an aliquot sum equal to the original number
3. ABundant numbers have an aliquot sum greater than the original
4. is less than
5. No negative numbers

DS:


Algo:


"""

class PerfectNumber:

    @classmethod
    def classify(cls, number):
        """
        Returns whether it is perfect, abundant, deficient
        """
        if number < 0:
            raise ValueError("Input must be a positive integer")

        potential_divisors = []

        for divisors in range(1, number):
            if number % divisors == 0:
                potential_divisors.append(divisors)
        
        _sum = sum(potential_divisors)

        if _sum  == number:
            return "perfect"
        elif _sum > number:
            return "abundant"
        else:
            return "deficient"
        


            