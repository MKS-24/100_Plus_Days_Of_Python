import time
waqt = time.strftime("%h:%m:%Y:%H:%M:%S")
print("Time howa hai : ",waqt)
hour = int(time.strftime("%H"))
if(6<hour<12):
    print("Good Morning!!")
elif(hour >= 12 and hour < 17):
    print("Good After Noon!!")
elif(hour >= 17 and hour < 20):
    print("Good Evening!!")
else:
    if(hour < 24):
        print("Good Night")
    else:
        print("Why you don't sleep?")
