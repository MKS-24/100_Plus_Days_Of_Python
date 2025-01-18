import os
folder = os.listdir("23_OS_Module/data")
print(folder)
print(os.listdir(f"23_OS_Module/data/01"))
for i in folder:
    print(i)
    print(os.listdir(f"23_OS_Module/data/{i}"))