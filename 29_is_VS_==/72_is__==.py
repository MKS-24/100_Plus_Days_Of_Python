# is batata hai exact location of object in memory 
# == batata hai value same hai

a = [1,2,3]
b = [1,2,3]
print(a is b) # exactlocation of object in memory  mera phone and baba ke bete ka phone same hai na
print(a == b) # value mera phone samsung wala aapka phone samsung wala same tu nh hoga na
   

c = 4
d = 4
print(c is d)
print(c == d)


e = (1,2,3)
f = (1,2,3)
print(e is f)
print(e == f)

g = "Khan"
h = "Khan"
print(g is h)
print(g == h)
# immutable per bhi same rahe ga == and is...