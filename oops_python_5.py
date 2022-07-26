from re import S


class Vehicle:
    _year = 1000 #notation for protected modifier 
    __price=10000 #denotes private variable


class TataMotors(Vehicle):
    car_name="Harrier"

v1 = Vehicle()
# print(dir(v1))
# print(v1.__price)
print(v1._Vehicle__price)

t1=TataMotors()
print(t1._year,v1._Vehicle__price)