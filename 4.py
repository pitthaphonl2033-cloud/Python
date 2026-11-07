num=int(input("Enter a number: "))
if num % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")


score=int(input("Enter your test score (0-100):"))
if score>=95:
    print("Your grade is: A+")
elif score>=90:
    print("Your grade is A")
elif score>=85:
    print("Your grade is B+")
elif score>=80:
    print("Your grade is B")
elif score>=75:
    print("Your grade is C+")
elif score>=70:
    print("Your grade is C")
elif score>=65:
    print("Your grade is D+")
elif score>=60:
    print("Your grade is D")
elif score<60:
    print("Your grade is F")
else:
    print("Invalid Score")


name=("Sam")
age=11
age=age+1
print(name, age)


name="Sam"
age=11
hobby="Gaming"
print(name, "is", age, "years old.")
print("Hobby:", hobby)


name=input("Enter your name")
print("Hello", name)
age = int(input("Your age?"))
print("Your current age is", age)
print("Next year you will be", age+1)


name=input("Name: ")
game=input("Favorite Game: ")
print("HELLO", name.upper())
print("You like playing",game.lower())


print ("Sprite  $3.45")
sprite=3.45
quantity=int(input("How many?"))
total= quantity*sprite 
print("Total: $", total)


a=int(input("First number: "))
b=float(input("Second number: "))
print("Sum:", a+b)
print("Product: ", a*b)


celcius=float(input("C: "))
kelvin=celcius+273.15
print("Kelvin:", kelvin)
celcius=float(input("C: "))
fahrenheit=(celcius*1.8)+32
print("Fahrenheit:", fahrenheit)
