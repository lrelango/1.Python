for temp in range(0,20):
    print(temp)
print("------------------------")
for temp in range(10,20):
    print(temp)

myList = [10, 20, 14, 55, 43, 87, 76]
print("Number of item in the List ", len(myList))

myText = "Artificial Intelligence"

for ch in myText:
    print(ch)

name = input("Enter a name :")
age = int(input("Enter the age"))
profession = input("Enter the profession")

print("-Your Name-", name)
print("-Your Age-", age)
print("-Your Profession-", profession)

tup = (1, 'Welcome', 2, 'Hope')
print(tup)

tup1 = (0, 1, 2, 3)
tup2=('python', 'HOPE')
tup3 = (tup1, tup2)
print(tup3)

list1 = [20,10,16,19,25,1,276,188]
for i in list1:
    if(i%2 ==1):
        print( i, "is odd number")

for i in list1:
    if(i%2 != 1):
        print(i, "is even number")