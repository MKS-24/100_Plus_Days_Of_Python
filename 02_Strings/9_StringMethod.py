# String immutable hoti hai 
# String me index ki value change nh hoti like name[0]="5"
# Har function se Copy banti hai
name="Muhammad Khuzaima Siddiqui!!!"
job="!!!Employee++"
hobby = "cricket"
name2 = "MUHAMMAD KHUZAIMA SIDDIQUI"
name3 = "   space    \n"
print(name)
print(len(name))
print(name.upper())
print(name2.lower())
print(job.rstrip("+")) # only end me joo character aata hai unko remove kerta hai
print(name3.strip()) # The .strip() method in Python removes leading (spaces at the start) and trailing (spaces at the end) whitespace characters from a string. It’s often used to clean up strings by removing unnecessary spaces or newline characters (\n, \r) at the beginning or end of a string.
print(name.replace("Khuzaima","Hamza"))
print(name.split(" "))  # bracket me wo likhte hai jaha se """"""""list"""""""" ke attribute ko break kerna hai
print(hobby.capitalize()) # only firstletter ko capital kerta hai
print(name.center(32,"*")) # * only dekhne ke liye likha ke space ko identify are * ke ilawa kuch oor bhi likh sahte hai
print(name.center(32))
print(name.count("K"))
print(name.endswith("i!!!")) # check kerta ke ke string ke end me give characters hote hai
print(name.endswith("K",2,10)) # 2 se 10 tak ke index ki string ke end me 'K' hai
print(name.isalpha())
print(hobby.isalpha())
dekhu = "my name is khuzaima siddiqui"
print(dekhu.title())
print(name.find("K")) # ye first occurance yani given sting jis string e find kerni hai us ka index return kertta hai
print(hobby.rjust(15,"*"))
print(hobby.ljust(15,"*"))
print(hobby.encode("utf-8"))
print("-".join(["hello", "world"]))

# imp=>
# print(name.index("k"))#  ye error return kare ga
# find and index same function hota hai lkn difference ye hota hai ke jab find wali string nh milti tu find function -1 return kerta hai
# lkn index function hum use kare orr index wali string ager nh mile tu -1 ki bajae program error writeen kare ga

print(job.isalpha()) #alpha check kerta
print(job.isalnum()) #alpha numeric check kerta
print(job.isnumeric())
print(hobby.islower())
print(name2.isupper())
print(job.isdecimal())
content = "lihku\n" # isme \n printable nh hai
content2="dekha"
print(content.isprintable())
print(content2.isprintable())
space = "space_nh_diya_beech_me"
x = " "
print(name.isspace())
print(x.isspace())  # only space hai tu
print(name.istitle()) # ye check kerta hai ke her new word ka first letter capital hona chahiye
print(hobby.istitle())
print(name.startswith("M"))
print(name.swapcase())  # small letter ko capital and capital letter ko small kerta hai
