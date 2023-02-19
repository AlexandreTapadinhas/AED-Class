# Rui Tapadinhas 2018283200

from sys import stdin,stdout

def readln():
  return stdin.readline().rstrip()

def outln(n):
  stdout.write(str(n))
  stdout.write("\n")

def readMatrix():
    n,m = [int(i) for i in readln().split()]
    matrix = []
    for i in range(n):
        line = readln().split()
        matrix.append([])

        for l in range(m):
            matrix[i].append(int(line[l]))
    return matrix


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            stdout.write(str(matrix[i][j]))
            if j != len(matrix[i]) - 1:
                stdout.write(" ")
        stdout.write("\n")

# code to rotate matrix 90 degrees clockwise
def rotate90(matrix):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            new_matrix[j][n - i - 1] = matrix[i][j]
    return new_matrix


if __name__ == "__main__":
    matrix = readMatrix()

    for i in range (3):
        matrixRot90 = rotate90(matrix)
        stdout.write(str(90 + 90*i))
        stdout.write("\n")
        printMatrix(matrixRot90)
        matrix = matrixRot90