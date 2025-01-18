import os
if not os.path.exists("23_OS_Module/data"):
    os.mkdir("23_OS_Module/data") #folder banadega
for i in range(0,5):
    os.mkdir(f"23_OS_Module/data/{i}")
    

