class Person:
    def __init__(self , n , o):        # har baar constructor call hota hai jab bhi new object banaya jae ga
        self.name = n
        self.occupation = o
    def __init__(self):
        print('Hey I am a person')
    def info(self):   # self ka matlab wo object jis per ye method or function call horaha hai
        print(f"{self.name} is a {self.occupation}")

a = Person("Harry" , 'Developer')   # yaha per 3 argument paas howe hai 1st = object , 2nd = n , 3rd = o
b = Person("Aslam" , 'Web Dev') 
b.info()
c = Person("Sanjay" , 'Mobile Dev') 
c.info()

d = Person(1,2,3) # ye error de ga QK parameter 4 paaas horahe hai 1st = object , 2nd = n , 3rd = o , 4th pata nh kiya tu Error aaega