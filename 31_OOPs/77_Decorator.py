# decorators functions ko modify kerte hai
def greet(fx):
    def mfx(*args , **kwargs):  # *args argument as a tuple leta and **kwargs as a dictionary value pair leta
        print('Good Morning')
        fx(*args , **kwargs)
        print("Thanks For Using This Function")
    return mfx

# @greet
def hello():
    print('Hello World')

def Name():
    print('My name is Khuzaima')


def add(a,b):
    print(a+b)

hello()
greet(Name)()   # @greet ye without function ke upper likha hai
greet(add)(1,2) 