a = input("Enter a Number : ")  # isme ager mene khuzaima likhdiya tu error aaega
print(f"Multiplication table of {a} is : ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")  # abhi ke liye error aaega


except Exception as ed:  
    print(ed)
    try:
        for i in range(1,11):
            print(f"{int(a)} X {i} = {int(a)*i}")  # abhi ke liye error aaega
    except Exception as ed:  
        print(ed)
        print(ord('A'))  # asii ke liye 

except:
    print("End of this program")