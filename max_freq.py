





def max_freq_of_a_word(file_path):
 file = open(file_path,'r')
 data = file.read()
 data = data.split()
 
 map_ = {}
 
 for value in data:
  if value in map_:
    map_[value] += 1
  else:
    map_[value] = 1
 
 return map_

map_ = max_freq_of_a_word('a.txt')
print(map_)

data = max_freq_of_a_word('a.txt')
file = open('collect.txt','w')
for k,v in data.items():
    file.write(k+' '+str(v)+'\n')




