with open('25_File_Handling/myfile2.txt','r') as t:
    t.seek(2)   # ye function kehta hai ke meri file ko tum 2 character of file se read karo
    print(t.read())
