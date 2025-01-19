# with open('25_File_Handling/myfile2.txt','r') as f:
#     while  True:
#         line=f.readline()
#         if not line:
#             break
#         print(line,end="")
i = 0
with open('25_File_Handling/myfile2.txt','r') as f:
    while  True:
        i += 1
        line = f.readline()
        if not line:
            break
        m1 = line.split(",")[0]
        m2 = line.split(",")[1]
        m3 = line.split(",")[2]
        print(f"Marks of Student {i} in maths is:{m1}")
        print(f"Marks of Student {i} in maths is:{m2}")
        print(f"Marks of Student {i} in maths is:{m3}")
        print(line,end="")

    