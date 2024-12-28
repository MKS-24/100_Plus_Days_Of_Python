alpha = "He Said"
print(alpha)
# ab ager aese print kerna hu "He Said , "He wants to go" " tu error aajae ga just because of double inverted commas ke
#  alpha = "He Said , "He wants to go"" #   -> error hai 
# is ko tackle kerne ke liye hum escape sequence(\) ka use kare ge like 
alpha = "He Said , \"He wants to go\"" # -> ab error nh hai
# ya phir bahir sigle inverted comma and andar double inverted comma like
alpha = 'He Said , "He wants to go"' # -> ab error nh hai
print(alpha)







# for multi slines string  we can use 3 sigle imverted commas or 3double inverted commas
likhu =''' kdhfhdndsfdhf
jhjksnfnff
fguddmsnfdsfjkf
dbjshdisajdam,dnasvd
kjfsdfldsf dfdsjkfhsjf ds fkjdsfhdsfd '''

likhu2 =""" Other ContentOther Content
Other Content
Other Content
Other Content """

print(likhu)
print(likhu2)     












name = "Khuzaima"
for i in name:  # yaha hum value ko access kerrahe hai mean 0 per jo value parhi hai vo do 1 per jo value parhi hai vo du
    print(i)

name2 = "Siddiqui"
for i in range(len(name2)):  # yaha i as an value lerahehai
    print(name2[i])


strr = "Kham"
if "Kh" in strr:
    print("yes")