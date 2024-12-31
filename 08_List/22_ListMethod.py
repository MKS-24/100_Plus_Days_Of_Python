lst = [9,2,2,5,2,8]
print(lst)
lst.append(99)
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
lst.reverse()
print(lst)
print(lst.index(99)) # first occurance ka index return kerdeta hai
print(lst.count(2))


# Important
first = [5,4,3]
second = first  # Second first ki copy nh hai bulke reffence hai ager Second ka koi element change kiya tu first ka wohi element change hoga jo second ka howa hai
second[0] = 105
print(first)
# aesa na hu isliye hum copy function ka use kerte hai

third = first.copy()
third[0] = 555
print(first,third,sep="\n")

first.insert(1,255)
print(first)
first.extend(third) # extend kerta ye hai ke first list ke end me third list ke elemets add kerdu
print(first)
first.pop() # mean last index ki value ko delete kerdu
print(first)
first.pop(2) # mean 2 index ki value ko delete kerdu
print(first)
