import random
from collections import defaultdict

def r5():
    return random.randint(0, 4)

def r7():
    while True:
        n = 5*r5() + r5()
        if n <= 21:
            return n%7


def main():
    frequency = defaultdict(int)
    for i in range(100):
        n = r7()
        frequency[n]+=1
    print(frequency)

main()