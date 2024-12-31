# Default Argument
def sum(a = 5 , b = 4):
    return a+b

#Required Argument
def avg(a,c=2):
    return (a+c)/2


print(sum())

#  keyword argument
print(sum(b=1))
print(sum(a=1))

#Required Argument
# print(avg()) # error aaega QK a ki value nh di hai