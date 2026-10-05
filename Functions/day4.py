# def sort_array(arr):
#    #arr.sort()
#    #return arr 
#    sorted_arr =sorted(arr)
#    return sorted_arr
              
# arr = [2,3,5,6,4,2,1]
# print(sort_array(arr))

# def Sum(*numbers):
#     return sum(numbers)
# print(Sum(1,2))
# print(Sum(1,2,3,4))
# print(Sum(1,2,3,4,5,6,7,8,9,10))

# def print_num(*numbers):
#     print(numbers)
# print_num(1,3,4,5,)
# print_num(1,2)


# def student(**details):
#     print(details)
# student(name = "Abhay", course = "B.Tech", age = 20)    

# def countdown(number):
#     if number==0:
#         return
#     print(number)
#     countdown(number-1)
# countdown(10)

# def count(number):
#     if number>=6:
#         return
#     print(number)
#     count(number+1)
# count(1)

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
print(fact(5))