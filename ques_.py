# file = open('demo.txt','r')
# data = file.read()
# data = file.readlines()
# def stud_info():
# map_ = {}
# while True:
#     if stud_info[0] in map_:
#             map_[stud_info[0]].add(stud_info[1])
#     else:
#             map_[stud_info[0]] = {stud_info[1]}
#                 # map_[stud_info[0]].add(stud_info[1])
#             return(stud_info())
#     print(data(map_))

def read_file_and_return_map(file_path):
 file = open(file_path,'r')
 data = file.readlines()
 map_ = {}

 for elem in data:
    sub, name = elem.split()
    
    if sub in map_:
        map_[sub].add(name)
    else:
            map_[sub] = {name}
 file.close()
 return map_

map_ = read_file_and_return_map('demo.txt')
print(map_)
