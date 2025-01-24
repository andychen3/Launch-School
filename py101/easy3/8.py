# https://launchschool.com/exercises/a78354e8

def get_grade(score1, score2, score3):
    mean = (score1 + score2 + score3) // 3
    match mean:
        case mean if 90 <= mean <= 100:
            return "A"
        case mean if 80 <= mean < 90:
            return "B"
        case mean if 70 <= mean < 80:
            return "C"
        case mean if 60 <= mean < 70:
            return "D"
        case mean if 0 <= mean < 60:
            return "F"



print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True