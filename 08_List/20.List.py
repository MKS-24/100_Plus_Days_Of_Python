# Mutable hoti hai
marks = [95,92,97,25,"Khanjee"]
print("  Marks =>",marks)
marks[0] = 100
print("  Marks =>",marks)
marks[1] = 500
marks[2] = 100
marks[3] = 100
print("  Marks =>",marks)  # hum change kersakhte hai
print("  Marks =>",marks[-4]) # negetive index ko len(list or string) se minus karo

if(7 in marks):
    print("yes")
if("Khanjee" in marks):
    print("yes")
else:
    print("No")

print("  Marks =>",marks[1:-1]) # Same Like Slicing Concept

# Jump index 

# print(  List[yaha se : yaha tak jao : Steps]  )
print("  Marks =>",marks[1:-1,2]) # Jump index

for i in [0,5,2,6,4]:
    print(i)