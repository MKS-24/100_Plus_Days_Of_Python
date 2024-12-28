age = int(input("Enter Your age : "))
print("Your age is : ",age)
if(age >= 18): #ager
    if (age > 50): #nahitu
        print("Now, You drive carefully")
    else:
        print("You can drive")
elif (age < 5): #nahitu
    print("No, You drive in your home")
else: #magar
    print('You can\'t drive')