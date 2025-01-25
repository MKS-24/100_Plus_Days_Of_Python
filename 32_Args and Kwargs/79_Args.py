def func(a,b,*args):
    print(f"{a,b}")
    print(*args)# *args will unpack the tuple and print individual elements without brackets
    print(args) # args will print the tuple as a whole, with brackets
    print(f'{args}')

    
func(1,2,3,4,5,6,7,8,9,10)