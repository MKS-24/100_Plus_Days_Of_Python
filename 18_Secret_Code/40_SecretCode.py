import random
answer = input("""
What do you want?
Encode or Decode : """)
word = input("Enter Word For Acheive : ")
if(answer.upper() == "ENCODE"):
    if(len(word) >= 3):                             # khan
        lst = list(word)                            # hank
        last = lst.pop(0)            # char char char hank char char char
        lst.append(last)
        lst = [chr(random.randint(0,120))]+[chr(random.randint(0,120))]+[chr(random.randint(0,120))] + lst + [chr(random.randint(0,120))]+[chr(random.randint(0,120))]+[chr(random.randint(0,120))]
        word = ''
        for i in lst:
            word += i
        print(f"Encoded Value : {word}")
    else:
        reverse = ''                                # of
        for i in range(len(word)-1,-1,-1):          # fo
            reverse += word[i]
        print(f"Encoded Value : {reverse}")
elif(answer.upper() == "DECODE"):              # char char char hank char char char
    if(len(word)>=3):                          #                hank
        lst = list(word)                       #                khan
        lst.pop(0)
        lst.pop(0)                            
        lst.pop(0)
        lst.pop(len(lst)-1)
        lst.pop(len(lst)-1)
        lst.pop(len(lst)-1)
        lst = [lst.pop(len(lst)-1)] + lst
        word = ''
        for i in lst:
            word += i
        print(f"Decoded Value : {word}")
    else:                                      # fo
        reverse = ''                           # of
        for i in range(len(word)-1,-1,-1):
            reverse += word[i]
        print(f"Decoded Value : {reverse}")