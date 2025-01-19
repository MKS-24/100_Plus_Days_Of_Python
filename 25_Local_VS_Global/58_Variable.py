variable = 4   # Mene yaha per global variable banaya 

def printvariable():
    variable = 10                   # Variale ki value change tu hoi hai lekin local variable ban ke 
    print("function ",variable)     # Output aaega 10 QK global variable ko local banaker value change ki hai

def changevariable():
    global variable  # ab koi local variable ko use nh kiya bulke global variable ko call kiya then next line me change kerdiya
    variable = 100   # yaha per global variable ko change kiya hai 


print(variable)    # Output aaega 4 QK global variable ko print kiya hai

printvariable() 
print(variable) 
variable = 7   # yaha per global variable ko change kiya hai 

print(variable)   # Output aaega 7 QK global variable change kiya hai

changevariable()  # ab function me global variable ko change kerdiya hai

print(variable)  # Output aaega 100 QK global variable ko print kiya hai

