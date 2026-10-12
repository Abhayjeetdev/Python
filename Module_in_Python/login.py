import otp

generated_otp = otp.generate_otp()
print("your otp is ", generated_otp)
email = "abc@gmail.com"
user_email=input("Enter your e-mail:")

user_otp = int(input("Enter your otp:"))
count = 0

while True:
    if generated_otp==user_otp and user_email==email:
        print("Logged in successfully")
        break
    else:
        user_email=input("Enter correct e-mail:")
        user_otp=int(input("Invalid Otp. Re-Enter correct otp:"))
        count+=1
    
    if count>2:
        print("You have tried to login several times.")
        break