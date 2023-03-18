#!/usr/bin/env python3
"""
Rui Alexandre Coelho Tapadinhas
2018283200

 ____            _      _          _____ 
|  _ \ _ __ ___ (_) ___| |_ ___   |___ / 
| |_) | '__/ _ \| |/ _ \ __/ _ \    |_ \ 
|  __/| | | (_) | |  __/ || (_) |  ___) |
|_|   |_|  \___// |\___|\__\___/  |____/ 
              |__/                       

"""

import time

db = {}
db_driver = {}
list_mats = []
end = False
merge_sort_count_switches = 0


def bubble_sort(list):
    init = time.time()
    switched = False
    count_switches = 0
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                count_switches += 1
                switched = True
        if switched == False:
            break
    end = time.time()
    print('Tempo de execução: ' + str(end - init))
    print('Número de trocas: ' + str(count_switches))


def shell_sort(list):
    count_switches = 0
    init = time.time()
    gap = len(list) // 2
    while gap > 0:
        for i in range(gap, len(list)):
            temp = list[i]
            j = i
            while j >= gap and list[j - gap] > temp:
                count_switches += 1
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        gap //= 2
    end = time.time()
    print('Tempo de execução: ' + str(end - init))
    print('Número de trocas: ' + str(count_switches))

def merge_sort(list):
    global merge_sort_count_switches
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                merge_sort_count_switches += 1
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

def merge_sort_time(list):
    global merge_sort_count_switches
    init = time.time()
    merge_sort(list)
    end = time.time()
    print('Tempo de execução: ' + str(end - init))
    print('Número de trocas: ' + str(merge_sort_count_switches))



if __name__ == '__main__':
    while (not end): 
        cmd = input().split(maxsplit=1)

        if cmd[0] == 'DIM_BD':
            num_cmds = int(cmd[1])

            for i in range(num_cmds):
                cmd = input().split(maxsplit=1)
                content = cmd[1].rsplit(maxsplit=2)
                if cmd[0] not in db:
                    db[cmd[0]] = []
                db[cmd[0]].append([content[0], content[1] + ' ' + content[2]])
            print('BD_ATUALIZADA')
            #print(db)

            # ordenamento
            list_mats = list(db.keys())
            #print(list_mats)
            # default python sort
            #list_mats.sort()

            # bubble sort
            bubble_sort(list_mats)

            # shell sort
            #shell_sort(list_mats)

            # merge sort
            #merge_sort_time(list_mats)

            #print(list_mats)


        elif cmd[0] == 'CONSULTA_MATRICULA':
            #print('entrei CONSULTA_MATRICULA')
            if cmd[1] not in db:
                print('REGISTOS NAO ENCONTRADOS')
                print('FIM')
            else:
                list_info = db[cmd[1]]
                for info in list_info:
                    for ind in range(len(info)):
                        if ind != len(info) - 1:
                            print(info[ind], end=' ')
                        else:
                            print(info[ind])
                print('FIM')

        elif cmd[0] == 'CONSULTA_CONDUTOR':
            #print('entrei CONSULTA_CONDUTOR')
            flag_found = False
            for mat in list_mats:
                for info in db[mat]:
                    if info[1] == cmd[1]:
                        print(mat, info[0])
                        flag_found = True
            if not flag_found:
                print('REGISTOS NAO ENCONTRADOS')
            
            print('FIM')



        elif cmd[0] == 'CONSULTA_BD':
            break # Take out for results
            #print('entrei CONSULTA_BD')
            """list_mats = list(db.keys())
            #print(list_mats)
            list_mats.sort()
            #print(list_mats)
            """

            for mat in list_mats:
                for info in db[mat]:
                    print(mat, end=' ')
                    for ind in range(len(info)):
                        if ind != len(info) - 1:
                            print(info[ind], end=' ')
                        else:
                            print(info[ind])
            print('FIM')

        elif cmd[0] == 'TCHAU':
            end = True
