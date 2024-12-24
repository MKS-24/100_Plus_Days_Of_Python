import time
waqt = time.strftime("%H:%M:%S")
print("time howa hai : ",waqt)
hour = int(time.strftime("%H"))
if(hour < 12 and hour > 6):
    print("Good Morning!!")
elif(hour >= 12 and hour < 5):
    print("Good Evening!!")
else:
    if(hour < 12):
        print("Good Night")
    else:
        print("Why you don't sleep?")
