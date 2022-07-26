class Student:
    def __init__(self,id,fname):
       # print("hello")
        self.id=id
        self.fName=fname
    def StudentInfo(self):
        print(self.id,self.fName)


        #id=1
   # fName="REGEX"


# constructor L=: function (memory allocate => object)
# object
# object = className()

#Student_John
s1=Student(10,"John")
s1.StudentInfo()
#print(s1.fName,s1.id)

s2=Student(11,"Sakshi")
s2.StudentInfo()
#rint(s2.fName,s2.id)
#print(s2.fName,s2.id)
