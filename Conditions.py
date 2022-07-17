fname = 'Arpit'
lname = 'Agarwal'

# if fname == 'Arpit':
#  print('yes first name is Arpit')
# else:
#  print('No first name is not Arpit')

# if fname == 'Arpit' and lname == 'Alok':
#       print('yes')
# else:
#        print('no')

# if fname == 'Arpit' and not lname == 'Agarwal':
#       print('yes')
# else:
#        print('no')

# if 'Arpit' in [a,b,c]:
#  print('yoj')
# elif 'i' in 'Arpit':
#   print('yes')
# elif 'k' in 'Alok':
#   print('nom')
# else:
#  print('no')

# s = input("enter a string")
# for i in s:
#     if(ord(i)%2==0):
#         print(i ,'at even ASCII')
#         print(ord(i))

# noi = input()
# noi = int(noi)
# lst = []
# for i in range(noi):
#     s_i = input('ENTER some input: ')
#     lst.append(s_i)
#     print(lst)

no_of_elements = int(input())
map_ = {
    'str' : [],
    'int' : [],
    'float' :[]
}


for i in range(no_of_elements):
    dt = input('Enter Datatype: ')
    value = input('Enter value for above datatype: ')
    if dt == 'str':
        map_['str'].append(value)
    elif dt == 'int':
            map_['int'].append(int(value))
    elif dt == 'float':
                map_['float'].append(float(value))
    else:
                    print('Please initialise a empty list for {dt}'.format(dt))
print(map_)


    
