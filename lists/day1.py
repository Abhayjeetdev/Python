list = [
    '10',10.0,'Ten', 10,"tom",45
]

print(list[0])
print(list[2][1])

#list Slicing
print(list[1:5])

#updation
print("initial list:",list)
list[1]='HELLO'
print(list)

#Append
list.append('success')
print('appended list:', list)

#insertion
list.insert(6,100)
print(list)