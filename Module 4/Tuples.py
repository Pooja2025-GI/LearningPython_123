# t0 = (1,7, 7.8, "Pooja", (1,8,6))
# t1 = 1,8,9,10
# l1 = 5, 9, 11, 12
# print(type(t0))
# print(type(t1))
# print(type(l1))
#
# l2=list(l1)
# print(type(l2))
# #length
# print(len(t0))
#
# #indexing
# print(t0[0])
# print(t0[-3])
#
# #Slicing

# Student1= (10001, "John")
# Student2= (78.5, 91, 98, 89)
#
# student_details= Student1+Student2
# print(student_details)
#
# t1= ("class 5", 5000)
# print(t1*3)
#
# print(3 in Student1)
# print(98 in Student2)
# print(88 in Student2)

t0= 1, 9, 11, 25, 89, 97, 89, 67, 67, 67, 67
print(t0.count(67))

print(t0.index(67)) #what is the index of 97 in tuple
#print(t0.index(17)) #what is the index of 97 in tuple

print(min(t0))
print(max(t0))
print(sum(t0))