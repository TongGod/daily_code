import random


def main():
    Machine = 4
    time = []
    for i in range(100):
        time.append(random.randint(1, 100))
    time.sort()
    time.reverse()
    print(time)
    total = [0, 0, 0, 0]
    for i in time:
        min_time = total[0]
        k = 0
        for j in range(1, 4):
            if min_time > total[j]:
                k = j
                min_time = total[j]
        total[k] += i
    print(total)
    return 0

main()
