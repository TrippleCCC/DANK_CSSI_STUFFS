"""This is my file


This is the first python file I have written, sort of (not really).
"""


print('Hello World!')

if 1 == 2:
    print("wuuuuut")
else:
    print('ha!')

x = 1
while x <= 5:
    print(x)
    print("HA!")
    x += 1
    #this is a comment
    # Other


for thing in range(5):
    print(thing)

for thing in "hello":
    print(thing)

my_list = [1,2,3,4,5]
for bob in my_list:
    print(bob)

for val in range(15, 100):
    print('{val} is divisible by 2: {donno}'.format(
        val=val, donno=val%2 == 0
    ))


def my_function():
    print('hello lunchtime')
    return 'hello lunchtime'

my_function()

def fizzBuzz(num):
    """Prints out "Fizz", "Buzz", or "FizzBuzz"
    depending on a numbers diviibility by 5 or 3

    Args:
        num: (int) Number that will be checked
    Returns:
        "Fizz" in the number is divisible by only 3,
        "Buzz" if the number is divisible by only 5,
        or "FizzBuzz" if the number is divisible by
        3 and 5.

    """

    if(num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")
    elif(num % 3 == 0):
        print("Fizz")
    elif(num % 5 == 0):
        print("Buzz")

def betterFizzBuzz(num):
    #print("{f}{b}".format(f = "Fizz" if num % 3 == 0 else "", b = "Buzz" if num % 5 == 0 else ""))
    return "{f}{b}".format(f = "Fizz" if num % 3 == 0 else "", b = "Buzz" if num % 5 == 0 else "")


def rangedFizzBuzz(bot, top):
    for i in range(bot, top+1):
        print(str(i) + " is " + str(betterFizzBuzz(i)))
