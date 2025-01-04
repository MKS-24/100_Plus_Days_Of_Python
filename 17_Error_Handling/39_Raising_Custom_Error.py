a = input("Enter Value between 5 and 10 : ")
if (a == 'quit'):
    pass
elif(int(a) < 5 or int(a) > 10):
    raise ValueError("Poka")