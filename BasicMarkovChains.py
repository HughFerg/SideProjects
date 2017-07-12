import random
import sys


def chain():

    n = int(raw_input("How many trials would you like to test? "))

    immutableN = n

    current = 0  # Starting at Marios

    mariosCt = 0
    caboCt = 0
    bwwCt = 0

    while n != 0:

        number = random.randint(0, 1000)
        # probablilites for restaurants where each has a probability of going
        # to another restaurant or going backwards
        if current == 0:

            mariosCt = mariosCt + 1
            sys.stdout.write("M")
            if number >= 880:        # probability of repeating (.12)
                current = 0
            elif number >= 500:
                current = 1         # probability of going to cabo from marios (.38)
            else:
                current = 2         # probability of going to bww from marios (.5)

            n = n - 1

        if current == 1:

            caboCt = caboCt + 1
            sys.stdout.write("C")
            if number >= 700:        # probability of repeating (.3)
                current = 1
            elif number >= 201:
                current = 0         # probability of going to marios from cabo(.499)
            else:
                current = 2         # probability of going to bww from cabo (.201)

            n = n - 1

        if current == 2:

            bwwCt = bwwCt + 1
            sys.stdout.write("B")
            if number >= 923:        # probability of repeating (.077)
                current = 2
            elif number >= 759:
                current = 0         # probability of going to marios from bww(.164)
            else:
                current = 1         # probability of going to cabo from bww (.759)

            n = n - 1

    return immutableN, mariosCt, caboCt, bwwCt


def main():

    n, m, c, b = chain()

    print("\nOut of %s trials..." % n)
    print("Marios: %s" % m)
    print("Cabo: %s" % c)
    print("BWW: %s" % b)


"""
Could probably calculate expected distribution of restaurants using matricies,
but hey
"""
if __name__ == "__main__":
    main()
