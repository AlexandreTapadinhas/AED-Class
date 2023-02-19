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
    ind_max1, ind_max2 = 0, 1

    for i in range(n):
        if array[i] > array[ind_max1]:
            ind_max2 = ind_max1
            ind_max1 = i
        elif array[i] > array[ind_max2]:
            ind_max2 = i

    max_sum = array[ind_max1] + array[ind_max2]

    end = time.time()
    exec_time = end - init
    print(exec_time)
    
    outln(max_sum)