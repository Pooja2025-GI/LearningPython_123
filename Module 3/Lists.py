name= "John"
Age= '20'
Percent= 80

# student1 = ["John", 20, 80]
# print(student1)
# print(type(student1))

days_of_week =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# print(days_of_week[3])
# print(f"first day of week is {days_of_week[0]}")

#length of the list

# print(len(days_of_week))
# print(f"last day of week is {days_of_week[-1]}")

#slicing of lists

l1 = [7,10,11,1, 2, 3, 3, 11, 2, 2, 2, 4, 5, 6, 7, 8, 9]
# print(l1[1:6:2])
# print(l1[1:6:1])
# print(l1[1:9:1])
# print(l1[1:9:3])

#concatenate list
l2 = [9, 8, 7, 6, 5, 4]
# print(l1 + l2)
# print(l2 + l1)

#repeatation of list

# print(l2*4)

#append list
#adding an item at the end of the list

Fruits= ["Apple", "Mango", "Orange"]
# print(Fruits)
# print(Fruits.append("Guava"))
# print(Fruits)

#insert adds an element at a specified location
#list.insert(index,item)

# Fruits.insert(2,"lichi")
# print(Fruits)

#extend() it can add multiple items in a single go unlike append where we can add only 1 item at a time
#remove()
#pop()

# Fruits.extend(["Pineapple", "Banana", "Peach"])
# print(Fruits)
#
# Fruits.remove("Apple")
# print(Fruits)
# Fruits.remove("Guava")
# print(Fruits)

# Fruits.pop(0)
# print(Fruits)

#reverse, sort, count, membership

# print(days_of_week)
# days_of_week.reverse()
# print(days_of_week)
#
# print(l1)
# l1.sort()
# print(l1)
# l1.sort(reverse=True)
# print(l1)
# print(l1.count(2))
# print(l1.count(7))
# print(l1.count(11))
# item_to_count= int(input(" Enter the number to be counted from l1:"))
# print(f"{l1.count(item_to_count)}")

print(3 in l1)
print(13 in l1)
print(4.33 not in l1)