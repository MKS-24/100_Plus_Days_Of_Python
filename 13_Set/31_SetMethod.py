
#  Set Theory wale concept hai

set1 = {1,2,3,4,5}
set2={3,4,5,6,7}
print(set1.union(set2))
set1.update(set2)
print(set1,set2)


s1 = {1,2,3}
s2 = {3,4,5}
print(s1.intersection(s2))
s1.update(s2)
print(s1)

ss1 = {1,2,3,4}
ss2 = {2,3,4,5}
print(ss1.symmetric_difference(ss2))

sss1 = {1,2,3,4}
sss2 = {2,3,4,5}
print(sss1.difference(sss2))

sss1 = {1,2,3,4}
sss2 = {2,3,4,5}
print(sss1.isdisjoint(sss2))  # koi intersection nh hu inme

ssss1 = {1,2,3,4}
ssss2 = {2,3,4}
print(ssss1.issuperset(ssss2))  
print(ssss2.issubset(ssss1))  

sone = {1,2,3}
print(sone)
sone.add(55)
sone.add(55)
print(sone)
sone.remove(55)
sone.discard(2)   #remove and discard same kaam kerte hai but error raire kerta hai remove but error raise nh kerta discard
print(sone)

one = {99,2,5,3,4}
print(one.pop()) # koi bhi random value delete kerta hai
print(one)

city={"Karachi" , "Multan"} # ager mujhe complete set ko delete kerna hai del ka use karo ga
print(city)
del city
# print(city)  # error raise hoga QK values hai hi nh tu print kya kare ga

# ager mujhe set chahiye lekin elements ko delete kerna hai only yani set ko empty kerna hai tu me clear use karo ga
two = {2,3,4,5}
print(two)
two.clear()
print(two)



