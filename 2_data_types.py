print("Please input your first name :")
f_name = input('First Name:')

print("Please input your second name :")
l_name = input('Last Name:')

print("Please input your age :")
age = int(input('Age: '))

# print("Hello,,.,.,you first name is,"  +f_name + " and your last name is", l_name)

# Another way to do the same thing using formatted strings

print(f"Hello,.,.,you name is  and your last name is,{f_name.capitalize} {l_name.capitalize} and your age is {age} years." )

print(f"In five years you will be {age + 5} ")
