# first_name = "John"
# last_name = "Doe"

# print(first_name.capitalize())
# print(last_name.capitalize())

# print(first_name.upper())

# last_name =last_name.casefold()
# print(last_name)

print("Enter Final Mark ")
student_mark = float(input("Enter Final Mark: "))

if student_mark >= 70:
    print("You have an A")
elif student_mark >= 60:
    print("You have a B")
elif student_mark >= 50:
    print("You have a C")
elif student_mark >= 40:
    print("You have a D")
else:
    print("You have an E")
