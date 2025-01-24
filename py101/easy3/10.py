# https://launchschool.com/exercises/a5eccabb

def century(year):
    remainder = year % 100
    century = year // 100

    if remainder != 0:
        century_value = str(century + 1)
        if century_value.endswith("11") or century_value.endswith("12") or century_value.endswith("13"):
            return f"{century_value}th"
        elif century_value.endswith("1"):
            return f"{century_value}st"
        elif century_value.endswith("2"):
            return f"{century_value}nd"
        elif century_value.endswith("3"):
            return f"{century_value}rd"
        else:
            return f"{century_value}th"

    elif remainder == 0:
        return f"{str(century)}th"


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True