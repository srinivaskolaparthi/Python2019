name = None

class Srini:
    def __init__(self, name,age):#constructor
        self.name = name
        # self.name is class variable
        # class variable scope is within a class.cannot access class variable
        #outside the class
        
        # name is local variable
        #local variable scope is with in a function
        self.age = age
        print("2 argument constructor invoked",name,age)

    def abcd(self):
        print("abcd activated",self.name)

b = Srini("kolaparthi",22)#no need to specify self while creating an object
b.abcd()
