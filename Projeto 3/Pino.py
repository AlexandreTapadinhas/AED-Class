""" 
# ======= Auxiliares =======
import time
import numpy as np
import matplotlib.pyplot as plt
import scipy
 
# ======================== Funções de tempos ========================

#tempos = list()


def get_graph(x_axis, y_axis, titulo):
    #Get the Linear regression
    R=scipy.stats.linregress(x_axis, y_axis)[2]
    #Build the plot
    plt.plot(x_axis, y_axis)
    plt.title(titulo)
    plt.xlabel("Quantidades")
    plt.ylabel('Tempo')
    #Ajustar de acordo com os dados
    
    plt.text(x_axis[len(quantidades)-1]/2,y_axis[1]/2, "R= {:.6f}".format(R),fontsize=15,bbox=dict(facecolor='white', alpha=0.5))
    plt.savefig("graf/"+titulo+".png")
    plt.show()
    
def getTimes(solucao):
    
    for qua in quantidades:
        start = time.time()
        if(solucao == 'A'):
            soma_exaustiva(qua)
        elif(solucao == 'B'):
            soma_ordenada(qua)
        elif(solucao == 'C'):
            soma_simples(qua)
        end = time.time()
        tempos.append(end-start)    
    fp = open("times.txt","a")
    
    fp.write("Solução "+solucao+"\n")
    for i in range(len(quantidades)):
        fp.write("For {} the time was: {}\n".format(quantidades[i],tempos[i]))
    
    get_graph(quantidades,tempos,"Solução "+solucao)
    tempos.clear()

def create_random_array(minimum, maximum, length):
    return np.random.randint(minimum, maximum + 1, size=length)
 """
# ======================== Tratamento dos dados ========================

def openFile(filename):
    fp = open(filename,'r')
    lines = fp.readlines()
    
    #Bidimensional list in which each line is a full case and the collumns have:
    #matricula,infracao,gravidade and name respectfully
    data = list(list())
    
    #Reads all the lines and separates the data 
    for text in lines:
        caso = str_to_list(text)
        data.append(caso)
    
    return data

def str_to_list(text):
    """ 
    This function receives a string of the data unorganized and returns a list with 4 elements in this order:
    matricula, infracao, gravidade, nome    
    """

    line = text.split()
    matricula = line[0]
    infracao = str()
    i = 1
    
    #Goes through the list until the next character is a digit, indicating that its the attribute "gravidade"
    while( not  (  line[i].isdigit())  ):
        infracao = infracao + line[i] + " "
        i+=1
    gravidade = line[i]
    i+=1
    name = ""
    
    #The rest of the chars belong in the name
    for aux in line[i:]:
        name = name + aux + " "
    infracao = infracao[:len(infracao)-1]
    name = name[:len(name)-1]
    caso = [matricula,infracao,gravidade,name]
    #print("Added: Matricula: {}, infracao: {}, gravidade: {}, name: {}".format(matricula,infracao,gravidade,name))
    
    return caso

# ======================== Functions ========================

def add_cases(bd, number):
    for i in range(number):
        caso = input()
        bd.append(str_to_list(caso))
    print("BD_ATUALIZADA")
    
def search_matricula(bd,matricula):
    found = 0
    for case in bd:
        if case[0] == matricula:
            found = 1
            print("{} {} {}".format(case[1],case[2],case[3]))
    if found == 0: 
        print("REGISTOS NAO ENCONTRADOS")
    print("FIM")

def search_condutor(bd,nome):
    found = 0
    for case in bd:
        if case[3] == nome:
            found = 1
            print("{} {} {}".format(case[0],case[1],case[2]))
    if found == 0: 
        print("REGISTOS NAO ENCONTRADOS")
    print("FIM")

def print_bd(bd):
    for casos in bd:
        print("{} {} {} {}".format(casos[0],casos[1],casos[2],casos[3]))
    print("FIM")

# ======= ORDENAMENTO ======
def compare(matricula1, matricula2):
    
    """ Esta funçao toma proveito do facto de um char alfa seja considerado maior do que um char digito.
    Desta forma percorre todos os caracteres da função até que seja encontrada uma diferença
    Returns:  -1 ->"m2 > m1"   0 -> "m2 = m1"       1 -> "m1 > m2"    """
    
    for i in range(len(matricula1)):
        if matricula1[i] > matricula2[i]:
            return 1
        elif matricula1[i] < matricula2[i]:
            return -1
    return 0

# ======= Elementar

def insertion_sort(bd):
    """ 
    Algoritmo ->
    1. Marca o primeiro membro como ordenado
    2. Marca um número como a chave
    3. Percorre a lista da direita para a esquerda e enquanto encontra elementos maiores do que a chave desloca-os para a direita
    4. Quando chega ao fim ou encontra um elemento mais pequeno, insere a chave à sua direita
    """
    
    #marca o primeiro como ordenado
    for i in range(1, len(bd)):
        key = bd[i]
        j = i - 1

        
        #Avança para trás enquanto a esquerda tiver numeros maiores que a chave
        #print("Key: {} and bd[j][0]: {}".format(key,bd[j][0]))
        while j >= 0 and ( compare(key[0],bd[j][0]) == -1):
            #Enquanto anda para trás passa todos os números maiores 1 posição para a direita
            bd[j + 1] = bd[j]
            #print("{} {}".format(bd[j + 1],bd[j + 1]))
            j = j - 1
        
        #Neste ponto já chegou ao fim ou encontrou um número menor, metendo então à sua direita a chave
        #Não há problema pois todos os outros passaram para a direita
        bd[j + 1] = key
    

# ======= Elementar


      
    
# ======= MAIN =======
def main():
    loop = 1
    #bd = openFile("matriculas.txt")
    #print_bd(bd)
    bd = list()
    
    
    while(loop):
        texto_entrada = input()
        entrada = texto_entrada.split()        
        
        if(entrada[0] == "TCHAU"):
            loop = 0
        
        elif(entrada[0] == "DIM_BD"):
            add_cases(bd, int(entrada[1]))
            insertion_sort(bd)
        
        elif(entrada[0] == "CONSULTA_MATRICULA"):
            search_matricula(bd,entrada[1])
        
        elif(entrada[0] == "CONSULTA_CONDUTOR"):
            name = str()
            for i in entrada[1:]:
                name = name + i + " "
            search_condutor(bd,name[:len(name)-1])
        elif(entrada[0] == "CONSULTA_BD"):
            print_bd(bd) 

main()