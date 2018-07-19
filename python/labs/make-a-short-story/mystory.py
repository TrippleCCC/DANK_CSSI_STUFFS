"""
My Story Lab

"""

lineOne = "The once was a {gen} named {n}."
lineTwo = "{n} liked {f}."
lineThree = "{n} once ate a lot of {f}s."
lineFour = "Afterwards, {n} felt really sick."
lineFive = "the end".upper()


gender = input("Male or Female?: ")
name = input("Give me a nice name: ")
food = input("What is your favorite food?: ")


print(lineOne.format(gen = gender, n = name))
print(lineTwo.format(n = name, f = food))
print(lineThree.format(n = name, f = food))
print(lineFour.format(n = name))
print(lineFive)
