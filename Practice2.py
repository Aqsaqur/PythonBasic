# write a program wap if a number entered by the user is odd or even 

num = int(input("enter number: "))

if num % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

# write the above program in nested loops



# wap to find the greatest of 3 numbers entered by the user.
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))

if a >= b and a >= c:
    print("the first number is largest")
elif b >= c:
    print("second is the largest")
else:
    print("third is the largest number")


# wap to check if a number is a multipule of 7 or not
x = int(input("enter number: "))

if x % 7 == 0:
    print("multiple of 7")
else:
    print("not a multiple")

