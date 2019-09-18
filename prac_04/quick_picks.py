from random import randint

quick_pick_lines = int(input("How many quick picks? "))

qps = []
all_quick_picks = []

for num in range(1, quick_pick_lines + 1):
    for i in range(1, 7):
        random_number = (randint(1, 45))
        while random_number in qps:
            random_number = (randint(1, 45))
        qps.append(random_number)
    qps.sort()
    all_quick_picks.append(qps)
    print("{:2} {:2} {:2} {:2} {:2} {:2}".format
          (qps[0], qps[1], qps[2], qps[3], qps[4], qps[5]))
    qps = []
