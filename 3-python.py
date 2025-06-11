i = int(input("Enter a number :"))
if i==10 :
    print("CORRECT")

password = input("Enter the password")
if password == 'Hope@123':
    print("Your password is correct")

age = int(input("Enter your age"))
if age<18:
    print("Children")
elif age <39:
    print("Adult")
elif age<59:
    print("Citizen")
else:
    print("Senior Citizen")

num = int(input("Enter any number"))
if num>0:
    print("The number is positive")
else:
    print("The number is negative")

num1 = int(input("Enter any number to check divisible by 5"))
if num1%5 == 0:
    print("The number {} divisible by 5".format(num1))
else:
    print("The number {} not div1isible by 5".format(num1))

list1 = [20,10,16,19,25,1,276,188]

def AgeCategory():
    for age in list1:
        if age < 18:
            print("Children")
            cate = "Children"
        elif age < 39:
            print("Adult")
            cate = "Adult"
        elif age < 59:
            print("Citizen")
            cate = "Citizen"
        else:
            print("Senior Citizen")
            cate = "Senior Citizen"
        return cate
    return None


AgeCategory()