#Palindrome means Reverse of String

 # We can do Palindrome by two types
 #1. Reverse String Method
#
# A = input("Enter a name: ")
#
# Rev = A[::-1]
# print(Rev)
#
# if A == Rev:
#     print("It is a palindrome")
# else:
#     print("Not a palindrome,Ok")

# BY Numbers

number = int(input("Enter a number: "))

temp = number
rev = 0
while (number > 0):
    dig=number%10
    rev=rev*10+dig
    number=number//10
if (temp == rev):
    print(" It is Palindrome")
else:
    print("Not a Palindrome")
