a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))
# FAlse

# The answer is true because a and c are pointing to the same place. B is also 
# because of interning. numbers from -5 to 256 locations are preassigned in
# Pyython