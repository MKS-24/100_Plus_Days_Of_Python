import random

def play_again():
    choice = input("""
\033[1mDo you Want To Play Again?
Answer : """)
    if choice.upper() == "YES" or choice == 1:
        return "YES"
    else: return "NO"


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
            print("\033[1mYou Won...\033[0m")
        elif(ans.upper() == tup[mix].upper()): 
            print("\033[1mDraw...\033[0m")
            continue            
        else: print("\033[1mYou Loss...\033[0m")
        if(play_again() == "NO"): flag = False

print("\033[1mAllah Hafiz\033[0m")

