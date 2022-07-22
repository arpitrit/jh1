# try:
#     print(5/0)
# except:
#     print("You can't divide by 0")    

try:
    print(5/'a')
except ZeroDivisionError:
    print("You can't divide by 0")
except TypeError:
        print("You can't divide by string")
except:
        print("Something went wrong")    