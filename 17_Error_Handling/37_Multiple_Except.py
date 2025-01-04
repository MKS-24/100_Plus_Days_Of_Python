try:
    num = int(input("Enter Number : "))
    lst = [10,15,20]
    print(lst[num])
except ValueError:
    print("Value is not an Integer")
except IndexError:
    print("Had me rehke index daalo")