Nonso = {"Name":"Nonso",
        "age": 18,
        "has_cat": False,
        "had_dog": True,
        "hair_color": "black"}

if __name__ == "__main__":
    print(Nonso)



class person(object):
    def __init__(self, name, age, has_cat, has_dog, hair_color):
        self.name = name
        self.age = age
        self.has_cat = has_cat
        self.has_dog = has_dog
        self.hair_color = hair_color
        self.hungry = True
        self.asleep = False

    def eat(self, food):
        print("GOT DAYYYYYYYMMMMM THAT WAS GOOOOOODDD")
        self.hungry = False

    def sleep(self):
        print("I'm going to sleep.")
        self.asleep = True

    def wake_Up(self):
        print("Guten Morgen!")
        self.asleep = False

    def __string__ (self):
        return 'My name is {self.name}'
