def square(value):
    return value * value

# Lamda Function ka use simply un functions ke liye hota hai jisme koi zyada kaam na hu
# like
square2 = lambda value2 : value2*value2 
#  ab ye square2 ko mene lamda ki help se single line me likha ye benefit hai
# lamda ka use small function ke liye kiya jata hai
word = lambda x: f"abcsefghijklmnopqrstuvwxyz{x}"
alphabets = lambda : f"abcsefghijklmnopqrstuvwxyz"

# print(square(5))
# print(square2(6))
print(word(500))
print(alphabets())