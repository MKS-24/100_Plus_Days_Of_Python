lst = [90,80,70,60,50]
# index = 0
# for i in lst:
#     print(index,i , sep="  ")
#     if(index == 2):
#         print(index,"Value" ,sep=" ")
#     index+=1

for index,i in enumerate(lst):
    print(index,i , sep="  ")
    if(index == 2):
        print(index,"Value" ,sep=" ")


for index,i in enumerate(lst,start=1):
    print(index,i , sep="  ")
    if(index == 2):
        print(index,"Value" ,sep=" ")
for index,i in enumerate(lst,start=-1):
    print(index,i , sep="  ")
    if(index == 2):
        print(index,"Value" ,sep=" ")
