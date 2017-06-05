'''
num = input('Enter a number ')
num = int(num)

if num % 2 == 0:
    print('%s is even!' % num)

else: print('%s is odd!' % num)

 ---------------------------------------

num = input('Enter a number ')
num = int(num)

a = range(1,num - 1)

for b in a:
    if num % b == 0:
        print('%s is a divisor of %s' % (b, str(num)))

--------------------------------------------------------

user1 = raw_input('First player move? ')
user2 = raw_input('Second player move? ')

keepGoing = True

global int1
global int2


def initializeAndCheck(user1):

    if user1 == 'r':
        int1 = 1
    elif user1 == 'paper' or 'p':
        int1 = 2
    elif user1 == 'scissors' or 's':
        int1 = 3

    return int1


def checkWinner(int1, int2):
    print int1
    print int2
    if int1 == int2:
        print('Its a tie!')
    elif int1 - int2 > 0:
        print("Winner: User1!")
    else:
        print("Winner: User2!")


def main():
    checkWinner(initializeAndCheck(user1), initializeAndCheck(user2))


if __name__ == "__main__":
    main()


'''


word1 = raw_input("Type your first word ")
word2 = raw_input("Type your second word ")


def check(word1, word2):

    if len(word1) > len(word2):
        temp = word1
        word1 = word2
        word2 = temp

    chars = []

    for a in range(0, len(word1)):
        chars.append(word1[a])

    count = 0

    for char in chars:
        if char not in word2:
            count += 1

    if count > 0:
        print("All letters in the smaller word are not in the larger word!")
    else:
        print("All letters in the smaller word are in the larger word!")


def main():
    check(word1, word2)


if __name__ == "__main__":
    main()
