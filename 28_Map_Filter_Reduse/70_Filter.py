def greater(n):
    return n%2
list1 = [1,2,3,4,5,6]
newlist = []
for i in list1:
    if i%2 == 0:
        newlist.append(i)

print(newlist)

list2 = [1,2,3,4,5,6]
newlist2 = list(filter(greater,list2))   # ye desired condition ke hisaab se nikalta hai
newlist3 = list(filter(lambda x: x%2==0,list2))   # ye desired condition ke hisaab se nikalta hai
newlist4 = list(filter(lambda x,y=1: (x+y)%2==0,list2))   # ye desired condition ke hisaab se nikalta hai
print(newlist3)


# Map sab per apply hoke show kerta hai all element
# Filter sab per apply hoke show kerta hai wo element jo satisfy kare condition ko