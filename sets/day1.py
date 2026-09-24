# set ={1,1,1,1,2,2,2,3,3,3,4,4,5,5}
# print(set)
# for i in set:
#     print(i)

# set = {1,1,7,8,9,2,3,3,7,8,6,5,6,3,4,4}
# #add
# set.add("abhay")
# #remove
# set.remove(6)
# #discard
# set.discard(10)
# print(set)

# set1={10,20,10,30,20,40,50}
# sum = sum(set1)
# print(sum)

# marks ={90,85,75,93,46}
# sum = sum(marks)
# length = len(marks)
# average = sum/length
# print(average)

# num = int(input("enter any number:"))
# sum = 0
# while num!=0:
#     sum = sum+num
#     num = int(input("enter any number:"))
# print(sum)

A={1,2,3,4}
B={3,4,5,6}
#union
print(A|B)
print(A.union(B))

#Intersection
print(A&B)
print(A.intersection(B))

#Difference
print(A-B)
print(A.difference(B))

print(B-A)
print(B.difference(A))

#Systematic differnce
print(A^B)
print(B^A)
