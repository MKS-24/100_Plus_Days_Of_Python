def square(value):
    return value * value


lst = [1,2,3,4,5,6,7,8,9,10]
nlst = []
for i in range(0,len(lst)):
    nlst.append(square(lst[i]))
print(nlst)

# ab itna sara code likhne ki bajae me simply ye karoga ke map ko use karo
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = list(map(square,list1))  # map obrect crate hogaya then usko jisme chahu convert kerdu 
list3 = list(map(lambda x: x*x*x , list1)) # lambda function bhi use kersakhte hai
print(list2)
print(list3)