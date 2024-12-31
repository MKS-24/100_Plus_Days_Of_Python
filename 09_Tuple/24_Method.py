# Immutable like string
tup = (1,1,2,"khan",3 , 5 , 3 , 9) 
print(tup.count(1))
print(tup.index(3))
print(tup.index(3,3,7))    #.index(value,start,end)    start , end me slicing hoti 
print(tup.index(3,5,7))
print(len(tup))
arr = list(tup)  # tuple change nh hosakhti inliye hum tup ko list banaker kisi me save kare ge then jo changes kerni hai wo list me kerlege
print(arr) 
arr.append(55)
arr.append(55)
print(arr) 
tup = tuple(arr) #list se tuple me change hogaya
print(tup)
tup1 = (1,2)
tup2 = (3,4)

tup1 += tup2 # concatinate hosakhti hai
print(tup1)


# tuple  ko ager edit kerna hai tu pehle list me convert karo
# jisse list ke all method use kersakhte hu
# then change ki hoi list ko tuple me convert kerdu  (Simple!!) 