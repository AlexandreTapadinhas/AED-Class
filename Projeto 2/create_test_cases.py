import random


if __name__ == '__main__':

    size = int(input("Size of test cases: "))

    with open('test_case_{}.txt'.format(size), 'w') as f:
        f.write(str(size) + '\n')
        for i in range(1, size + 1):
            n = random.randint(1, 100000)
            if (i == size):
                f.write(str(n))
            else:
                f.write(str(n) + ' ')