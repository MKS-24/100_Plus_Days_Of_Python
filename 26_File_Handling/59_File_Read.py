# v = open('25_File_Handling/myfile.c++','r')   # r mode default hota hai tu mrzi hai likhu ke nh lekin likhna bhtrr hai
v = open('25_File_Handling/myfile.c++','rt')   # rt mode default hota hai tu mrzi hai likhu ke nh lekin likhna bhtrr hai
# v = open('25_File_Handling/myfile.c++','rb')   # rb mode hota hai ke file ager binary formate me likhnii hai
text = v.read()
print(text)
text = v.close()