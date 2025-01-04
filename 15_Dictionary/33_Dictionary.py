students = {
    17 : "Muhammad Rafay Anwar",
    29 : "Muhammad Khuzaima Siddiqui",
    27 : "Abdul Rehman",
    11 : "Muneeb"
}

# print(students)


# print(students[17])
# print(students.get(27))


# print(students.keys())
# for i in students.keys():
#     print("Keys hai ",i,"and value hai",students[i])


print(students.items())
print()
for i,k in students.items():
    print(f"The value corresponding to the key {i} is {k}")
    print(f"The value corresponding to the key {i} is {students[i]}") # both ways are correct