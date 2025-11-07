
#საშინაო დავალება N1

num_list = [44, 23, 11, 8, 20, 56, 33, 55]

a = float(input("Enter a number: "))

if a in num_list:
    print("The number in list")
else:
    print("The number not in list")


#საშინაო დავალება N2

a = int(input("Enter a integer: "))

if a % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#საშინაო დავალება N3

st1 = "good"
st2 = "good"

if st1 is st2:
    print("Same object")
else:
    print("Different object")


#საშინაო დავალება N4

num_list = [44, 23, 11, 8, 20, 56, 33, 55]

a = int(input("Enter a number: "))

if num_list[2] < a < num_list[len(num_list)-1]:
    print("More than list elements")
elif a == num_list[5]:
    print("Equal")
else:
    print("None of the conditions were met")
