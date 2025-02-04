print(0.3 + 0.6) # .8999
print(0.3 + 0.6 == 0.9) # FAlse

# The reason my original assumption was wrong because of floating point precision
# If you want to get the right answer you would have to use the math module

import math

print(math.isclose(0.3 + 0.6, 0.9))