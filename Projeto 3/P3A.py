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

db = {}
db_driver = {}
list_mats = []
end = False


def bubble_sort(list):
    switched = False
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                switched = True
        if switched == False:
            break
        switched = False


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
            #merge_sort(list_mats)

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
