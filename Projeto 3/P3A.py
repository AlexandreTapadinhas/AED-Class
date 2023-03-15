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
            # ordenamento
            list_mats = list(db.keys())
            #print(list_mats)
            list_mats.sort()
            #print(db)


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
