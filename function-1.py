def AgeCategory():
    global cate
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


list1 = [20,10,16,19,25,1,276,188]
listVal = AgeCategory()
print(listVal)

def oddEven():
    num =int(input("Enter a number"))
    if num%2 == 0:
        print("The number {} is even number".format(num))
    else:
        print("The number {} is odd number".format(num))

oddEven()

def Bmi():
    bmi = int(input("Enter the bmi index  : "))
    if bmi <= 18.5:
        print("You are underweight.")
        bmi = "You are underweight."
    elif 18.5 < bmi <= 24.9:
        print("Your weight is normal.")
        bmi = "Your weight is normal."
    elif 25 < bmi <= 29.29:
        print("You are overweight.")
        bmi = "You are overweight."
    else:
        print("You are obese.")
        bmi = "You are obese."
    return bmi

bmIndex = Bmi()
print (bmIndex)

def add(num1, num2):
    return num1+num2

print(add(5,4))