class person:    # class ban gai just like form
    name = "Harry"
    occupation = "Softare Developer"
    networth = 10
    def info(self):   # self ka matlab wo object jis per ye method or function call horaha hai
        print(f"{self.name} is a {self.occupation}")



a = person()  # object ban gaya just like form fill of first Student
a.name = 'Khuzaima'
a.occupation = "Student"
a.networth = 600
print(a.name , a.occupation , a.networth) 
a.info()


b = person()  # object ban gaya just like form fill of first Student
b.name = 'Siddiqui'
b.occupation = "Student"
b.networth = 700
print(b.name , b.occupation , b.networth)
b.info()


c = person()  # object ban gaya just like form fill of first Student
c.name = 'khan'
c.occupation = "Student"
print(c.name , c.occupation , c.networth)  # ab jab networth print hogi wo , wo wali hogi jo by defalut mene di thi
c.info()

