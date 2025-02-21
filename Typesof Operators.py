"""
1. Arithmetic Operators
Used for mathematical operations.

Operator	Description	Example (a = 10, b = 3)	Result
+	Addition	a + b	13
-	Subtraction	a - b	7
*	Multiplication	a * b	30
/	Division (floating-point)	a / b	3.3333
//	Floor Division	a // b	3
%	Modulus (Remainder)	a % b	1
**	Exponentiation (Power)	a ** b	1000
2. Comparison (Relational) Operators
Used to compare values, returning True or False.

Operator	Description	Example (a = 10, b = 3)	Result
==	Equal to	a == b	False
!=	Not equal to	a != b	True
>	Greater than	a > b	True
<	Less than	a < b	False
>=	Greater than or equal to	a >= b	True
<=	Less than or equal to	a <= b	False
3. Logical Operators
Used for logical operations.

Operator	Description	Example (x = True, y = False)	Result
and	True if both are True	x and y	False
or	True if at least one is True	x or y	True
not	Inverts boolean value	not x	False
4. Bitwise Operators
Used to perform bit-level operations.

Operator	Description	Example (a = 5 (0101), b = 3 (0011))	Result
&	AND	a & b	1 (0001)
`	`	OR	`a
^	XOR	a ^ b	6 (0110)
~	Bitwise NOT	~a	-6
<<	Left Shift	a << 1	10 (1010)
>>	Right Shift	a >> 1	2 (0010)
5. Assignment Operators
Used to assign values to variables.

Operator	Description	Example (a = 10)	Equivalent to
=	Assigns value	a = 5	a = 5
+=	Add and assign	a += 3	a = a + 3
-=	Subtract and assign	a -= 3	a = a - 3
*=	Multiply and assign	a *= 3	a = a * 3
/=	Divide and assign	a /= 3	a = a / 3
//=	Floor divide and assign	a //= 3	a = a // 3
%=	Modulus and assign	a %= 3	a = a % 3
**=	Exponentiate and assign	a **= 3	a = a ** 3
&=	Bitwise AND and assign	a &= 3	a = a & 3
`	=`	Bitwise OR and assign	`a
^=	Bitwise XOR and assign	a ^= 3	a = a ^ 3
<<=	Left shift and assign	a <<= 1	a = a << 1
>>=	Right shift and assign	a >>= 1	a = a >> 1
6. Identity Operators
Used to compare object identity (memory location).

Operator	Description	Example (a = [1,2,3], b = a, c = [1,2,3])	Result
is	True if objects have the same identity	a is b	True
is not	True if objects have different identity	a is not c	True
7. Membership Operators
Used to check if a value exists in a sequence (list, tuple, string, etc.).

Operator	Description	Example (lst = [1,2,3])	Result
in	True if value exists in the sequence	2 in lst	True
not in	True if value does not exist in sequence	5 not in lst	True

"""

# 8. Ternary Operator (Conditional Expression)
# A shorthand for if-else statements.


x = 10
y = 20
min_value = x if x < y else y  # Returns 10
print(min_value)


"""
9. Operator Precedence
Python follows precedence rules when evaluating expressions:

Precedence Order (from highest to lowest):

() – Parentheses
** – Exponentiation
+x, -x, ~x – Unary plus, minus, bitwise NOT
*, /, //, % – Multiplication, division, floor division, modulus
+, - – Addition, subtraction
<<, >> – Bitwise shift operators
& – Bitwise AND
^ – Bitwise XOR
| – Bitwise OR
==, !=, >, >=, <, <=, is, is not, in, not in – Comparison operators
not – Logical NOT
and – Logical AND
or – Logical OR
if-else – Conditional expression
lambda – Lambda function

"""

# arithmetic operators
a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # this gives reminder
print(a ** b) # this gives a to the power of b a^b


# Relational / comparion operators 
c = 50
d = 60

print(c == d) # False
print(c != d) # True 
print(c >= d) # True 
print(c <= d) # False

# assignment operators 
num = 10
num += 10
print("num", num) # 20

# logical operators 
print(not False) # not of false
print(not True) # not of true


