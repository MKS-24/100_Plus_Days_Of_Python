class Employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id

    def showdetail(self):
        print(f"Employee Name is {self.name}")
        print(f"Employee id is {self.id}")

    @property
    def Name(self):
        return self.name
    
    @Name.setter
    def Name(self,newname):
        self.name = newname

    @property
    def Id(self):
        return self.id
    
    @Id.setter
    def ID(self,newID):
        self.id = newID


e1 = Employee('Muhammad' , 9024)
e1.showdetail()
e2 = Employee('Khuzaima' , 9204)
e2.showdetail()
e3 = Employee('Siddiqui' , 9224)
e3.showdetail()
