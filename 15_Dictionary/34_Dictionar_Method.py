data1 = {"one":1 , "two":2 , 3 :"Three"}
data2 = {2:"two","two":2}
 

data1.update(data2) # set ki tarha dictionay bhi value repeat nh kerta  
print(data1)

one = {2:"two","two":2}
print(one)
one.clear() # clear kerta hai value ko
print(one)
 
one = {}
print(one)
one.clear()
print(one)

one={2:"two","two":2}
one.pop("two")
print(one)


one={2:"two","two":2}
one.popitem()   # Last Element ko remove kerta hai
print(one)

one={2:"two","two":2}
print(one)
# del one
print(one)

one={2:"two","two":2}
print(one)
del one[2]
print(one)

