#  1. Personal Information, Create variables to store
# Your Name
# your age
# your favorite number
# print all values in a single statement
import numbers
#
# Name = "Lithish"
# Age = 27
# Fav_Num = 9
# print(Name,Age,Fav_Num)

# 2. Simple calculation
#   Create two variables with numbers.
#   print
#      Their sum
#      Their Difference
# #      Their Product
# A = 9
# B = 6
# print("Sum of two numbers:",A+B)
# print("Difference of two numbers:",A-B)
# print("Product of two numbers:",A*B)
#3
#
# shopping bill calculator
# shoe = 60
# shirt = 35
# T_shirt = 15
# # print("Total_Bill_Amount",shoe+shirt+T_shirt)
# for i in range(0,10):
#     print(i+1)
# for i in range(1,21):
#
#     if i % 2 == 0:
#         print(i)
#     else:
#         print("The number you entered is not even number")

# x = int(input("Enter a number: "))
# for i in range(1,11):
# #     print(x,"*",i,"=",x*i)
# x = int(input("Enter a number: "))
# for i in range(1,8):
#     print("Day",i,":",x,"steps")
# # x = (input("Enter a P or N: ").upper())
# for i in range(1,11):
#         print("Student",i,": Present")
    # else:
    #     print("Student",i,": Not Present")
    #
    #
# x = int(input("Enter one  item cost"))
# for i in range(1,11):
# #     print(x," * ",i," = ",x*i)
# i = 1
# total = 0
# while i <= 50:
#     total = total + i
#     i = i + 1
# print(total)

password = 'abc@123'
user = ""
while user != password:
    user = input("Please enter your password: ")
    if user == password:
        print("Welcome your password is correct! ")
        break

secret_number = 7
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess == secret_number:
        print("Correct! You guessed the number.")
        print("Total attempts:", attempts)
        break
    else:
        print("Wrong guess. Try again.")

savings = 0
days = 0

while savings < 1000:
    savings += 50
    days += 1

print("Total savings:", savings)
print("Total days required:", days)


correct_username = "admin"
correct_password = "1234"

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Welcome! Login successful.")
        break
    else:
        print("Invalid credentials. Try again.")


units = int(input("Enter units consumed: "))
bill = 0

if units <= 100:
    bill = units * 5
else:
    bill = (100 * 5) + ((units - 100) * 7)

print("Total Electricity Bill: ", bill)









