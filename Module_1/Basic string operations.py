s1= "hello World"
type (s1)

s2= "we are learning python"
type (s2)

s3 = """ Hello Everyone. We are learning python"""
type (s3)


print(type(s1))
print(type(s2))
print(type(s3))
print(len(s1))

###indexing- how to find the position of characters###
###positive indexing start from left to right, starts from zero
###negative indexing start from right to left, starts from -1.

print(s3[4])
print(s3[-4])

###joining of string or concatenation of strings

print(s1+s2)
print(s1+' '+s2)