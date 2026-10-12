num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
print("Sum of two numbers:", num1+num2)
print("Difference two numbers:", num1-num2)
print("Product of two numbers:", num1*num2)
print("Division of two numbers:", num1/num2)

radius = float(input("Enter the radius:"))
area = 3.14 * radius **2
print("Area of the circle:", area)

length = float(input("enter length of retangle:"))
breadth = float(input("enter breadth of retangle:"))
print("Area of the rectangle:", length*breadth)

temp = float(input("enter the temperature(in degree celcius):"))
fahrenheit = (((9/5)*temp)+32)
print("Temperature in Fahrenheit:",fahrenheit)

sub1 = int(input("enter marks in Maths:"))
sub2 = int(input("enter marks in Physics:"))
sub3 = int(input("enter marks in Chemistry:"))
sub4 = int(input("enter marks in Hindi:"))
sub5 = int(input("enter marks in English:"))
total_marks = sub1+sub2+sub3+sub4+sub5
print("Total Marks:", total_marks)
percentage = (total_marks/5)
print("Overall percentage(%):",percentage)

initial_price = float(input("Enter the initial price:"))
gst = initial_price * 0.18
bill_amount = initial_price + gst
print("Total bill amount:",bill_amount)

salary = float(input("enter the salary amount:"))
bonus= salary*0.10
new_salary = salary+bonus
print("Salary with 10% bonus:", new_salary)

total_minutes = int(input("enter total minutes:"))
hours = total_minutes//60
minutes = total_minutes%60
print(f"Time--{hours}hr:{minutes}minutes")

num = int(input("enter a 3-digits number:"))
if len(str(num))!=3:
    print("Not valid number. Re-enter only 3- digit number")
else:
    digits_sum = (num//100) + ((num//10)%10) + num%10
    print("sum of digits:", digits_sum)

num = float(input("enter a number:"))
num%=5
print("Remainder when divided by 5:",num)

principle = int(input("Enter the principle amount:"))
rate = int(input("input rate(%):"))
time = int(input("enter time period (in years):"))
simple_interest = (principle*rate*time)/100
print("simple interest is:", simple_interest)

weight = float(input("Enter your body weight:"))
height = float(input("Enter your height in metres:"))
BMI = weight/height
print(f"Body Mass Index(BMI) is {BMI} ")

basic = int(input("enter basic salary :"))
pf = int(input("enter PF amount:"))
hra = int(input("enter HRA amount:"))
medical = int(input("enter medical allowances:"))
ta = int(input("enter travel Allowances:"))
net_salary = basic+pf+hra+medical+ta
print(f"Net salary is {net_salary}")
