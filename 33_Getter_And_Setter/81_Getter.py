class myclass:
    def __init__(self,value):
        self.value = value

    def show(self):
        print(f"Value is {self.value}")

    @property   # getter bangaya 
    def defvalue(self):
        return 10*self.value

obj = myclass(10)
obj.show()
print(obj.defvalue)  # isse hota ye hai ke aap function ke saat calculations kersakhte hai