x = 5
print(x)
y = "hello"
print(y)
z = 3.141
print(z)
f = None
print(f)
t = True
print(t)
print(f"{x},{y},{z},{t},{f}" , sep=";")  # sep ka function f ke saat kaam nh kerta    f baad me parhe ge
print(x,y,z,f,t,sep=";")


print(type(x),type(y),type(z),type(f),type(t),sep="\n")   # family means class batata hai ke assign value number hai , character hai ya etc
print(id(x),id(y),id(z),id(f),id(t),sep="\n")     # id is like address

# Python me her cheez object hoti hai