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

    for i in range(n):
        for j in range(i+1,n):
            if i != j:
                sum = array[i] + array[j]

                if sum > max_sum:
                    max_sum = sum

    end = time.time()
    exec_time = end - init
    print(exec_time)
    
    outln(max_sum)