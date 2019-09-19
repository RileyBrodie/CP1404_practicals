from random import randint

quick_pick_lines = int(input("How many quick picks? "))

QPS = []
ALL_QUICK_PICKS = []

for num in range(1, quick_pick_lines + 1):
    for i in range(1, 7):
        random_number = (randint(1, 45))
        while random_number in QPS:
            random_number = (randint(1, 45))
        QPS.append(int(random_number))
    QPS.sort()
    ALL_QUICK_PICKS.append(str(QPS))
    print("{:2} {:2} {:2} {:2} {:2} {:2}".format
          (QPS[0], QPS[1], QPS[2], QPS[3], QPS[4], QPS[5]))
    QPS = []
