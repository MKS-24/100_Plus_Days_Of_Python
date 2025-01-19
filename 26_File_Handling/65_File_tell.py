with open('25_File_Handling/myfile2.txt','r') as t:
    t.seek(5)   # ye function kehta hai ke meri file ko tum 2 character of file se read karo
    print(t.tell())  # jaha tak seek kiya wa hai wo bata ta hai
    print(t.read())
