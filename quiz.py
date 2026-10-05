# num = int(input("Enter a number:"))
# reverse = 0
# while num>0:
#     digit = num%10
#     reverse = reverse*10+digit
#     num= num//10
# print(reverse)

# num = int(input("enter any num:"))
# sum = 0
# while num>0:
#     digit = num%10
#     sum = sum + digit
#     num = num//10
# print(sum)

# name = "abhay"
# print(name[5::-1])
# reverse = ""
# for char in name:
#     reverse = char + reverse
# print(reverse)

# password = 1234
# code = int(input("Enter passcode: "))
# while code != password:
# 	code = int(input("Incorrect passcode. Try again: "))
# print("Access granted")

# name = "python"
# new_name = ""
# for i in name:
#     new_name= new_name+i
#     print(new_name)
   
# sum = 0 
# for i in range(101,0,-1):
#     sum = sum+(i*i)
# print(sum)     

while True:
    num1 = float(input("Enter 1st number:"))  
    num2 = float(input("Enter 2nd number:"))  

    operator =input("Enter any operator from (+,-,*,/):")

    if operator=="+":
        print(num1+num2)
    elif operator=="-":
        print(num1-num2)
    elif operator=="*":
        print(num1*num2)
    elif operator=="/":
        if num2!=0:
            print(num1/num2)
    else:
        print("Please choose valid operator from the given list.")
    

while True:
    B_weight = float(input("Enter your body weight(in kg):"))
    h = float(input("Enter your height (in foot):"))
    height = h*0.3048 #coverting height in metre from foot
    
    Bmi = B_weight/(height**2)
    print("Your body mass index is", Bmi)
    
    if Bmi<18.5:
        print("underweight")
    elif 18.5<=Bmi<=24.9:
        print("Normal")
    elif 25<=Bmi<=29.9:
        print("Overweight")
    else:
        print("obese")
    
    