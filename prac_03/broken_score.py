def main():
    score = float(input("Enter score: "))
    score_result = score_grader(score)
    print(score_result)


def score_grader(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
