file = open('demo.txt','r')
# data = file.read()
data = file.readlines()
file.close()
print(data)


# write a file
file = open('demo.txt','w')
file.write('This is a demo file\n')
file.writelines('Monday is a good day\ngood is bad')
file.close()

# append a file
file = open('demo.txt','a')
file.write('This is a demo file2')
file.close()