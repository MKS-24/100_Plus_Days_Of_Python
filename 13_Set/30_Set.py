# set is a collection of well defined object
# set me koi bhi value repeat nh hoti duplicate value allow nh kerta
# Order maintain kerne ki koi guarntee nh hai koi value kisi bhi index per aajati hai
# yaha hum curly bracket used kerte hai
# immutable

value = [1,2,2,2,3]
value2 = (1,2,2,2,3)
value3 = {1,2,2,2,3}

for i in value3:
    print(i , end=" ")


x = {}   # ye empty set nh banata ye dictionary ka formate hai
print(type(x))   # ye empty set nh banata ye dictionary ka formate hai


# Empty set banane ke liye yu likhte hai
y = set()
print(type(y))
print(type(value3))


