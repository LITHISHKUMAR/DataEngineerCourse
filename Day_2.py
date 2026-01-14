# a=5
# b=6
# print("a=" + str(a)+,+"b="+ str(b)"sum:")
#
# x=int(input("enter any number"))
# y=int(input("enter any number"))
# if x>0:
#     print("x is greater than 0")
# elif x<0:
#     print("x is less than 0")
# elif y<20:
#     print("y is less than 20")
# else:
#     print("y is greater than 20")

#
# students =["lithish","reddy","sai","kumar"]
# for i in students:
#     if(i=="sai"):
#         print(i)

# word ="HeLLo PyTHon"
# for i in word:
#     print(i.upper())

#
# count = 1
# while count <= 5:
#     print(count)
#     count +=1

#
# marks= int(input("Enter marks: "))
# if marks >= 90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")
# elif marks >= 70:
#     print("Grade C")
# elif marks >= 60:
#     print("Grade D")
# else:
#     print("Grade F")



secret_number = 7
guess = 0
while guess != secret_number:
    guess = int(input("guess the number(1-10)"))
    if guess < secret_number:
        print("too low")
    elif guess > secret_number:
        print("too high")
print("congratulations! you gusssed it.")