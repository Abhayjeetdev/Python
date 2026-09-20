'''WRONG LOGIC'''
# num = input("Enter any number:")
# digit_sum = 0
# if num == '0':
#     print("You entered 0 as a number so sum of digit is also 0")
# else:
#     for digit in range(len(num)+1):
#         digit_sum += digit
# print(f"Sum Of all the digits of number you enterd is {digit_sum}")


'''CORRECT LOGIC'''

# num = int(input("Enter any number:"))
# digit_sum = 0
# while num!=0:
#     digit  = num%10
#     digit_sum+=digit
#     num//=10
# print("Sum of all the digits of the number you entered is",digit_sum)

