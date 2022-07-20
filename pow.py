s = input()
map_ = {}
for i in s:
    if i in map_:
        map_[i] += 1
    else:
        map_[i] = 1
print(map_)

n = input()
n = n.lower()
map_ = {}
for i in n:
    if i in map_:
        map_[i] += 1
    else:
            map_[i] = 1
print(map_)






lst = []
while True:
    commands = input()
    commands = commands.split()
    if commands[0] == 'stop':
        break
    elif commands[0] == 'push':
        lst.append(commands[1])
    elif commands[0] == 'pop' :
        index_of_value = lst.index(commands[1])
        lst.pop(index_of_value)
    else:
     print('Invalid Command')
print(lst)



map_ = {}
while True:
    stud_info = input()
    stud_info = stud_info.split()
    if stud_info[0] == 'stop':
        break
    else:
        if stud_info[0] in map_:
            map_[stud_info[0]].add(stud_info[1])
        else:
                map_[stud_info[0]] = {stud_info[1]}
                map_[stud_info[0]].add(stud_info[1])
print(map_)




