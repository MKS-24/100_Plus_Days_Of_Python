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
Answer : """)
# print("\033[0m")
flag = True
if choice.upper() == "YES" or choice == 1:
    while(flag == True):
        tup = ("rock","paper","Secciors")
        print(tup)
        ans = input("... ")
        mix = random.randint(0,2)
        print(f"""
🖥️  => {tup[mix]} 
🙋 => {ans}
""")
        
        if(ans.upper() == tup[mix].upper()): print("You Won...")
        else: print("You Loss...")
        if(play_again() == "NO"): flag = False

print("Allah Hafiz")

