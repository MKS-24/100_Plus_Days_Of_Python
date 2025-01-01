def fact(n):
    if(n==0 or n==1): return 1
    return n*fact(n-1)

def fibonaci(n):
    if (n==0) : return 1
    if(n==1): return 1
    return fibonaci(n-1) + fibonaci(n-2)



print(fact(5))
print(fibonaci(40))
