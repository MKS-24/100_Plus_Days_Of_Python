num = int(input("Enter Value of num : "))
match num:
    case 0:
        print("Khatam!!")
    case 1:
        print("Start!!")
    case 2:
        print("Start-Above")
    case _ if(3 <= num <=10):
        print("Value 3 se 10 take me se hai")
    case _ if(num >= 5 and num <=100):
        print("Value 10 se 100 tak hai")  
    case _:
        print("Default case chalgaya")

#  isme break statment nh likhte
# jo pehle hit kiya wo chale ga and break kerde ga match ko