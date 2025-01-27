class Employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id
        print("dfhd")

    def showdetail(self):
        print(f"Employee Name is {self.name}")
        print(f"Employee id is {self.id}")

class programmer( Employee ): #Class programmer me Employee ke all Function accessable hai
    def showLanguage(self):
        print("Python")


e1 = Employee('Muhammad' , 9024)
e1.showdetail()
e2 = Employee('Khuzaima' , 9204)
e2.showdetail()
e3 = programmer('Siddiqui' , 9224)
e3.showdetail()
e3.showLanguage()

