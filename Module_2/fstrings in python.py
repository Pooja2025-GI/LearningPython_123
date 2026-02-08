### formatting strings

name ="john"
age = 32
language = "python"
hours = 3

# john is 32 years old. He studies python 3 hours a day.

print(name,"is", age, "years old.He studies", language, hours,"hours a day.")

#using f-string
print(f"{name} is {age} years old.He studies {language} {hours} hours a day")

sub1= 85
sub2= 87
sub3= 74

print(f"{name} scored {sub1 + sub2 + sub3} marks in total")