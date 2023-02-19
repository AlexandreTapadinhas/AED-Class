# Rui Tapadinhas 2018283200

from sys import stdin,stdout
import time


def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write("\n")

if __name__ == "__main__":
    n = int(readln())
    input_array = readln().split()

    init = time.time()

    array = [ int(input_array[i]) for i in range(n) ]
    max_sum = 0
    array.sort(reverse=True)

    max_sum = array[0] + array[1]

    end = time.time()
    exec_time = end - init
    print(exec_time)
    
    outln(max_sum)