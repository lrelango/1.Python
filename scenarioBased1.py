# To check age eligible to vote or not
age = int(input("Enter your age: "))
if age >= 18:
    print("You are Eligible to vote")
else:
    print("You are not Eligible to vote")

#To find largest value in the list

list1=[4,7,65,87,67,40]
#largest=max(list1)
largest=0
for i in list1:
    if i > largest:
        largest = i
print(f"The largest value in the list is: {largest}")

#To calculate the bonus as per salary

salary = int(input("Enter your salary: "))
bonus=20000
if salary > 50000:
    bonus=bonus+salary * (10/100)
print(f"Your bonus is: {bonus}")

#4--To check given number is even or not--

num=int(input("Enter a number: "))
if num % 2 == 0:
    print(f"The number {num} is even")
else:
    print(f"The number {num} is odd")

#5--Reverse the given string--

text = "Hello World"
reversed_text = text[::-1]
print(reversed_text)

#6-To check whether given score is passed or not-

score = int(input("Enter your score: "))
passing_score=40
if score >= passing_score:
    print(f"You have passed and Your score is: {score}")
else:
    print(f"You have failed and Your score is: {score}")

#7-20% discount on order value > 100-

totalOrder = int(input("Enter your totalOrder: "))
if totalOrder>=100:
    totalOrder=totalOrder- totalOrder*(20/100)
print(f"Your total order value is: {totalOrder}")

#8- Allow to withdraw sufficient balance-

totalBalance=int(input("Enter your total balance: "))
withdrawAmount=int(input("Enter your withdraw amount: "))
minimumBalance=1000
if withdrawAmount <= (totalBalance-minimumBalance):
    print(f"You can withdraw the amount and amount is: {withdrawAmount}")
else:
    print(f"You don't have enough money to withdraw the amount: {withdrawAmount}")

#9-Finding given year is leap or not-

year=int(input("Enter your year: "))
if (year % 4 == 0) and (year%100 != 0) or (year%400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#10-getting even numbers from the list-

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [i for i in numbers if i%2 == 0]
print(even_numbers)
