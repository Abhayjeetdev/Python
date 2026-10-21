# # num1=int(input('enter number'))
# # num2=int(input('enter number'))
# # try:
# #     div=num1/num2
# #     print(div)
# # except ZeroDivisionError:
# #     print('enter non zero number')

# num1=10
# num2='20'
# try:
#     sum=num1+num2
#     print(sum)
# except TypeError:
#     print('declare type')

list=[1,2,3,4,5]
try:
    print(list[6])
except IndexError:
    print('index out of bound')