import random
import string

f = open("input_1000k.txt", "w")
f.write('DIM_BD 1000000\n')
for i in range(1000000):
    palavra = ''
    linha = ''
    matricula = str(random.choice(string.ascii_letters)) + str(random.choice(string.ascii_letters)) + str(random.randint(10, 99)) + str(random.choice(string.ascii_letters)) + str(random.choice(string.ascii_letters)) + ' '
    linha += matricula
    for k in range (random.randint(2, 5)):
        for j in range (random.randint(3, 14)):
            palavra += random.choice(string.ascii_letters)
        linha += palavra + ' '
        palavra = ''
    linha += ' ' + str(random.randint(0, 5)) + " "
    for k in range (2):
        for j in range (random.randint(5, 10)):
            palavra += random.choice(string.ascii_letters)
        linha += palavra + ' '
        palavra = ''

    f.write(str(linha) + '\n')

f.write('CONSULTA_BD\nTCHAU')
f.close()