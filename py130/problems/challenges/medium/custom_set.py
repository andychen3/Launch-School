# https://launchschool.com/exercises/546a7352

"""
input:
output:
rules:

DS:


Algo:

"""
class CustomSet:

    def __init__(self, my_set=[]):
        self.my_set = my_set

    @property
    def my_set(self):
        return self._my_set
    
    @my_set.setter
    def my_set(self, my_set):
        res = []
        for num in my_set:
            if num not in res:
                res.append(num)
        self._my_set = res

    def is_empty(self):
        return len(self.my_set) == 0
    
    def contains(self, num):
        return num in self.my_set
    
    def is_subset(self, custom_set):
        if self.is_empty():
            return True
        
        if custom_set.my_set == self.my_set:
            return True

        return all((True if num in custom_set.my_set else False for num in self.my_set ))
    
    def is_disjoint(self, custom_set):
        if self.is_empty() or custom_set.is_empty():
            return True
        
        return all((False if num in custom_set.my_set else True for num in self.my_set ))
    
    def is_same(self, custom_set):
        return sorted(custom_set.my_set) == sorted(self.my_set)
    
    def add(self, num):
        if num not in self.my_set:
            self.my_set.append(num)

    def __eq__(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented
        
        return sorted(self.my_set) == sorted(other.my_set)
    
    def __ne__(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented
        
        return sorted(self.my_set) != sorted(other.my_set)
    
    def intersection(self, custom_set):
        res = [num for num in self.my_set if num in custom_set.my_set]
        return CustomSet(res)

    def difference(self, custom_set):
        res = [num for num in self.my_set if num not in custom_set.my_set]
        return CustomSet(res)
    
    def union(self, custom_set):
        self.my_set.extend(custom_set.my_set)
        return CustomSet(self.my_set)


