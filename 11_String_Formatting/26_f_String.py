firstname="Muhammad"
middlename = "Khuzaima"
lastname = "siddiqui"

completename="my name is {} {} {}"
print(completename.format(middlename,firstname,lastname))
print(completename)



# easy steps to formatting
print(f"my name is {firstname} {middlename} {lastname}")
print(f"my name is {{firstname}} {{middlename}} {{lastname}}")


point = 45.4556542
print(f"value {point:.3f}")

print(f"{2*3}")  #string hai ye
print(type(f"{2*3}"))  