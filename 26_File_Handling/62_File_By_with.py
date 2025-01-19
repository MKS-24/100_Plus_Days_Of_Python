
with open('25_File_Handling/myfile2.txt','r') as f:
    print(f.read())

# write
with open('25_File_Handling/myfile2.txt','w') as f:
    f.write("write")

# append
with open('25_File_Handling/myfile2.txt','a') as f:
    f.write("\nappend")
# with se file khudhi close hojati hai