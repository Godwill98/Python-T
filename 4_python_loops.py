

# Create a list of possible values
# values = [2, 3, 4, "apple", "banana", "cat", "dog"]

# Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# for i in values:
#     for v in Days:
#         print(i,v)

count = 0

while (count <= 10):
    print (f"Counter is currently at {count}")
    if (count%2 == 0):
        print(f"{count} is even")
    else:
        print(f"{count} is odd")
    count += 1

