class Driver:
    def __init__(self,id,name,email):
        self.id=id
        self.name=name
        self.email=email

    def infoPrint(self):
       print("hello")
       #print(self.id,self.name,self.email)


class Customer(Driver):
    def __init__(self, id, name, email,wallet):
        super().__init__(id,name,email)
        self.wallet=wallet
       # print("hello")


# d1=Driver(1,"abc","abc@gmail.com")
# d1.infoPrint()

# c1=Driver(1,"abc","abc@gmail.com")
# c1.infoPrint()

c1=Customer(1,"john","john@gmail.com",100)
print(c1.name,c1.wallet)
