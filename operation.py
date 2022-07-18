s = 'Arpit is backend developer'
print(s.split())
s = 'Arpit-is-backend-developer'
print(s.split('-'))


# n =  int(input("Enter a no."))

# for i in range(n):
#     operation = input('enter operation string: ')
#     operation_list = operation.split()
#     print(operation_list)
#     if operation_list[0] == 'add':
#         fir_no = int(operation_list[1])
#         sec_no = int(operation_list[2])
#         print(fir_no + sec_no)
#     elif operation_list[0] == 'sub':
#             fir_no = int(operation_list[1])
#             sec_no = int(operation_list[2])
#             print(fir_no - sec_no)
#     elif operation_list[0] == 'mult':
#             fir_no = int(operation_list[1])
#             sec_no = int(operation_list[2])
#             print(fir_no * sec_no)  
#     elif operation_list[0] == 'div':
#             fir_no = int(operation_list[1])
#             sec_no = int(operation_list[2])
#             print(fir_no / sec_no)


# n = int(input("Enter a no."))
# for i in range(n):
#     op_ = input('enter op string: ')
#     op_list = op_.split()
#     m = len(op_list)
#     if op_list[0] == 'add':
#         add = int(0)
#         for j in range(1,m):
#             add = add + int(op_list[j])
#         print(add)
#         m = len(op_list)
#     elif op_list[0] == 'mult':
#             mult = int(1)
#             for j in range(1,m): 
#              mult = mult * int(op_list[j])
#             print(mult)


# n = int(input())
# for i in range(1,n):
#  n = n * i
# print(n) 


# n = int(input("Enter a no."))
# s = ''

# for i in range(n):
#     j = int(input())
#     s += chr(j)
#     print(s)