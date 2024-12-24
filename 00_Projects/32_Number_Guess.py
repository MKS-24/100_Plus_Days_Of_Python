import random

print("\t\t\t\033[1m Welcome To The Word Guessing Game \033[0m")
choice = input("""\033[1m
What Do You Want?
1.Start The Game
2.Exit From Game
\033[0mAnswer : """)
again = "YES"
question = ["ali","Aslam",3,"nice",5,"exit",7,"ok",9,10]
if(choice.upper() == "START" or choice.upper() == "1"):
    while(again.upper() == "YES"):
        print(f"\n{question}")
        answer = input("\nWhich One You Want To \033[1mChoose\033[0m : ")
        save = str(question[random.randint(0,len(question)-1)])
        flag = False
        for i in range(len(question)):
            if type(question[i]) == int:
                question[i] = str(question[i])
            if question[i].upper() == answer.upper():
                flag = True
                break
        if flag == True:
            if(save.upper() == answer.upper()):
                print(f"\n\033[1mCongrats!\033[0m You guessed {save} the correct Value!")
            else:
                print(f"\n\033[1mUnfortunately\033[0m, the option you guessed is wrong.\nThe correct option is {save}.")
                print("\n\033[1m\t\t----Game Over!!----\033[0m")
            again = input("\nDo You Want To Play Again?\nAnswer : ")
        else:
            print("\nPlease, Enter The Value Correctly..")
else:
    print("\033[1m\t\t----Allah Hafiz----\033[0m")