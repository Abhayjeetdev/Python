# def Sum(a,b):
#     return a+b
# print(Sum(10,20))

# def Sub(a,b):
#     return a-b
# print(Sub(20,10))

# def Mul(a,b):
#     return a*b
# print(Mul(20,10))
    
# # def greet():
# #     print("Hello World!!")
# # greet()

# # def greet():
# #     print("Good Evening")
# # greet()


def calc(a,b):
    return a+b, a-b, a*b, a/b

Sum, diff, product, div = calc(20,10)
print("sum:", Sum)
print("difference:", diff)
print("product:", product)
print("division:", div)