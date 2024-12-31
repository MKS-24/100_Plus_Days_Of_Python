#  break use kiya jata hai loop se bahir nikalne ke liye
#  continue use kiya jata hai iteration skip kerne ke liye
strr = "abcdef" # 0 1 2 3
for i in strr:
    if (i  > 'b' and i < 'd'):
        print("\nSkippp the iteration")
        continue
    elif(i == 'e'):
        print("\nbreak ker gaya loop ko")
        break
    print(i,end="")