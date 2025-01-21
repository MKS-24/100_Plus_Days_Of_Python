from functools import reduce
def sum(x,y):
    return x+y

list1 = [1,2,3,4,5]
newlist = reduce(sum,list1)
print(newlist)

#  ye puri list ke all element per operation apply kerke output deti hai