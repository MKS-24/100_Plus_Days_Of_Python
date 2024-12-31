name = "Khan"
for l in name:
    print(l,end="")


for c in range(5):
    print(c)
print()
for j in range(5,9):
    print(j,end="")

print()
for j in range(5,9):
    print(j,end="")
    j = j+2
    print(j)

print()

for j in range(10,9,-1):
    print(j,end="")
print()
# Ascending order
for i in range(2, 6, 1):
    print(i, end=" ")
# Descending order
for j in range(2, 6, -1):
    print(j, end=" ")
else:
    print("ff")
# for j in range(starting point,ending point,index):
#     print(j,end="")
#     j = j+2
#     print


# Python ke for loop mein aap directly loop variable (e.g., i) ko modify karte hain to uska loop iteration par koi asar nahi hota. 
# Iska reason yeh hai ke Python ka for loop kisi sequence (string, list, etc.) ke elements par iterate karta hai, 
# aur loop variable har iteration mein sequence ke agle element ko assign kar leta hai.