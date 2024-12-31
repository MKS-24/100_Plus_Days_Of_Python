lst = [i for i in range(4)]
print(lst)
lst = [i for i in range(5) if i%2 == 0]
print(lst)
lst = [i for i in range(5) if i%2 == 0 or i==4]
print(lst)

lst = [i for i in range(8) if i%2 == 0 and i<=4]
print(lst)

lst = [i*i for i in range(8) if  i<=3]
print(lst)

lst = [i for i in range(8,12)]
print(lst)

lst = [i for i in range(8,12) if i==9]
print(lst)


x = [1,2,3]
y = [4,5,6]
x += y
print(x) # concatinate hosakhti hai