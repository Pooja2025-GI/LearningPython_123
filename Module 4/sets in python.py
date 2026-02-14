#sets are non-sequential collection of items
#comma separated elements enclosed with in {}
#can not have indexing or slicing in sets
#sets do not allow duplicate items

set1= {10, 10, "False", "sagar"}
print(set1)
print(len(set1))

#membership

print("False" in set1)
print("sagar" not in set1)

#concatenation can not be done

set2= { 2, 6, 9, 11}
# print(set1 + set2)

#repeating can also not be done in sets

weekdays= ("Mon", "Tue", "Wed", "Thurs", "Fri")
print(weekdays)
weekdays= set(weekdays)
print(weekdays)

#sets are mutable

weekdays.add("Sat")
print(weekdays)
weekdays.remove("Thurs")
print(weekdays)
weekdays.discard("Mon")
print(weekdays)