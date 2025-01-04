def fun():
    try:
        l = [1,5,7,9]
        i = int(input("Enter Number : "))
        print(l[i])
        return 1
    except:
        print("Error")
        return 0
    finally:
        print("Ye lazmi chalega") # return hone ke bawajoooooood chale ga

x = fun()
print(x)