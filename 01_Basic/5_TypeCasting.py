x = "abc"
y = "def"
print(x+y) # string concatinate(+) hojati hai

one = "1" # as a character
two = "2" # as a character
print(one+two) # string concatinate(+) hojati hai

# Explicit Conversion mean jo hum khud kerwate hai
print(int(one)+int(two)) # string concatinate(+) hojati hai
a = int(one)
b = int(two)
print(a+b)

# Implicit Conversion mean jo Python khud kerta hai

f = 2.55
g = 1
print(int(f)+g)  # ye emplicit howa
print(f+g) # ye implicit howa mean 'f' float hai jabke 'g' integer hai tu same data tupe add hoti hai
# python khud 'g' ko float me convert kerke 'f' se add kare ga