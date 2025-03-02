# conditional statements
"""if-elif-else (syntax)
syntax means correct way to write code """

# checking if user can get driver licences or not by using if statement 
age = int(input("Enter Your Age:"))
# if age is greater equal to 18
if age > 18:
    print("Can apply of licences")
elif age < 18:
    print("You can't apply for licences")   
else: 
    print("wrong input")

#  traffic ligths

lights = str(input("Enter Traffic ligth Colour: ")).lower()

if lights == 'green':
    print("You Can drive")
elif lights == 'red':
    print("Stop!! You can't drive")
elif lights == 'yellow':
    print("Get Ready For Green Light")
else:
    print("Wrong Value!!")

# Grade students based on marks
marks = int(input("Enter Your %: "))

if marks >= 90:
    print("A")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >= 70 and marks < 80:
    print("C")
else:
    print("D")

print("Grade of the student ", marks)

# nesting
age2 = int(input("Enter Your Age: "))

if age2 >= 18:
    if age2 >= 80:
        print("You Cannot drive")
    else:
        print("You Can drive")
else:
    print("invaild input")
