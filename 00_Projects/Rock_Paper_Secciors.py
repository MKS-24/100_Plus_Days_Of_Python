# import math
# import random
# import smtplib

# digits = '0123456789'
# OTP = ""
# for i in range(5):
#     OTP += digits[math.floor(random.random()*10)]
# otp = OTP + 'is you One Time Password (OTP)!'
# send = smtplib.SMTP('smtp.gmail.com',587)
# send.starttls()
# send.login("programify.official@gmail.com" , '')
# useremail = input("Enter your Email : ")
# send.sendmail("kuch bhi",useremail,otp)
# check = input("Enter Your OTP : ")
# if check == OTP:
#     print("Verified")
# else:
#     print("Check Again !")
#     wbmdjtefwxktwbae


import math
import random
import smtplib

def play_again():
    choice = input("""
\033[1mDo you Want To Play Again?
Answer : """)
    if choice.upper() == "YES" or choice == 1:
        return "YES"
    else: return "NO"


digits = '0123456789'
OTP = "".join(random.choices(digits, k=5))  
useremail = input("Enter your Email: ")

subject = "Your One Time Password (OTP)"
body = f"Your OTP is: {OTP}"
message = f"Subject: {subject}\n\n{body}"  

send = smtplib.SMTP('smtp.gmail.com', 587)
send.starttls()
send.login("programify.official@gmail.com", "wbmdjtefwxktwbae")  

# Email Send Karna
send.sendmail("programify.official@gmail.com", useremail, message)

flagforotp = True
while(flagforotp):
    check = input("Enter Your OTP: ")
    if check == OTP:
        flagforotp = False
        Score = 0
        choice = input("""
\033[1mDo you Want To Play Game?
Answer \033[0m : """)
        flag = True
        if choice.upper() == "YES" or choice == 1:
            while(flag == True):
                tup = ("rock","paper","Secciors")
                print("\033[1m",tup,"\033[0m")
                ans = input("\033[1m... \033[0m")
                flag2 = False
                for i in tup:
                    if i.upper() == ans.upper():
                        flag2 = True
                if(flag2 == False): 
                    print("\033[1mEntered The Value Correctly!! \033[0m")
                    continue
                mix = random.randint(0,2)
                print(f"""
        🖥️  => {tup[mix]} 
        🙋 => {ans}
        """)     
                if(ans.upper() == tup[1].upper() and tup[mix].upper() == tup[0].upper()) or (ans.upper() == tup[2].upper() and tup[mix].upper() == tup[1].upper()) or (ans.upper() == tup[0].upper() and tup[mix].upper() == tup[2].upper()): # ans paper and computer rock
                    Score+=1
                    print("\033[1mYou Won...\033[0m\t\t\tHigh Score",Score)
                elif(ans.upper() == tup[mix].upper()): 
                    print("\033[1mDraw...\033[0m\t\t\tHigh Score",Score)
                    continue            
                else: print("\033[1mYou Loss...\033[0m\t\t\tHigh Score",Score)
                if(play_again() == "NO"): flag = False

        print("\033[1mAllah Hafiz\033[0m")

    else:
        print("Check Again!")
        check = input("Enter Your OTP: ")

send.quit()  
