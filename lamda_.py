# x = lambda a, b: a+b
# x(2,4)
# y = x(2,4)
# print(y)

# y = lambda n:[i for i in range(n)]
# z = y(5)
# print(z)

# power = lambda n:[i*2 for i in range(n)]
# w = power(6)
# print(w)

def is_even(n):
    return n % 2 == 0
a = filter(is_even,[1,2,33,276,675,34,65])
a = list(a)
print(a)

for i in a:
    print(i)