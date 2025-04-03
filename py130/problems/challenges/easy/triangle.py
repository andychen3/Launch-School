# https://launchschool.com/exercises/5f93085a?track=python

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.sorted_tri = self._check_valid(self.side1, self.side2, self.side3)

    def _check_valid(self, side1, side2, side3):
        sorted_tri = sorted([side1, side2, side3])
        if sum(sorted_tri[:2]) <= sorted_tri[2]:
            raise ValueError
        
        return sorted_tri

    @property
    def kind(self):
        if len(set(self.sorted_tri)) == 1:
            return "equilateral"
        elif len(set(self.sorted_tri)) == 2:
            return "isosceles"
        else:
            return "scalene"


    @property
    def side1(self):
        return self._side1
    
    @side1.setter
    def side1(self, side1):
        if side1 <= 0:
            raise ValueError
        
        self._side1 = side1

    @property
    def side2(self):
        return self._side2
    
    @side2.setter
    def side2(self, side2):
        if side2 <= 0:
            raise ValueError
        
        self._side2 = side2

    @property
    def side3(self):
        return self._side3
    
    @side3.setter
    def side3(self, side3):
        if side3 <= 0:
            raise ValueError
        
        self._side3 = side3