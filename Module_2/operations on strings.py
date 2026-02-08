s1= "python is fun"

#membership operator"in"

#print("python" in s1)
#print("u" in s1)

#print("b" in s1)

#print("q" not in s1)

#comparison of strings

#print("Python" == "Python")
#print("Python" == " Python")

# Removing spaces from a string is done using -strip()

#s1= "  Python "
#print(s1)
#s2= s1.strip()
#print(s2)

##Replace function replace()

s3= "We are learning python3.13 and it is fun"
#print(s3)
#print(s3.replace("fun","not fun"))
#print(s3)
#print(s3.replace("i","I"))
#print(s3.replace("i","I",2))


#Counting substring in a string
#count()
#string.count(substring)

#s1="We are learning Python. Python is fun. I am good at Python."
#s2=("e")
#print(f"occurence of {s2} is {s1.count(s2)}")

#cases in python(upper, lower, proper
#upper(), lower(), title(), capatilize()

print(s3.upper())
print(s3.lower())
print(s3.title())
print(s3.capitalize())

## starting with and ending with

print(s3.startswith("We"))
print(s3.startswith("fun"))
print(s3.endswith("fun"))
print(s3.endswith("n"))


