import random
RandomNumber=random.randint(1,300)
## if I want to show the number I have to print(RandomNumber)
userInput =int(input("Guess the number:"))
if userInput > RandomNumber :
    print(RandomNumber)
    print("The number is too high")
elif RandomNumber>userInput :
    print(RandomNumber)
    print("The number is too low")
else :
     print(RandomNumber)
     print("yes,you matched the number")


