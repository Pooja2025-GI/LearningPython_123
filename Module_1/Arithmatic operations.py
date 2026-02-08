###arithmatic operators
###+ add
### - Subtract
### * multiplication
### / divide
### // floor division(only integer value)
### % modulus(gives remainder as output)
### ** exponent
from packaging.markers import Marker

x=104
y=25
z=73
a=78
b=10.65
c=-456

print(a+b)
print(b-c)
print(c/x)
print(x*y)
print(x%4)

d= a+b+c
print(d)

e= (x+y+z)/3
print(e)

print(5**3)

###assignment operators is used to assign variables
###like =, +=, -+, *+, /=
###compound assignment operator
### x+ = which means x=1 works similarly for other operators as well.

x += 1
print(x)

###comparison & logical operators
### == equals to
### != equals to
### < equals to
### > equals to
### >= equals to
### <= equals to
num1= 100
num2= 90
num3= 90

print(num1 == num2)
print(num2 == num3)
print(num1 >= num2)

# logical opearators- And, OR, NOT
# AND False if any of the statement is False
# OR  True if any of the statement is True
# NOT result is always inverse

Name= "Mark"
Age= 25

Name == "Mark" and Age == 25
print(Name == "Mark" and Age == 25)