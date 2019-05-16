# I tend to think of a class as more of a 'framework' or a 'set of instructions' for building an object.
# in this example, i've created a class called 'Dog'.


class Dog:
    # The __init___ method is always called when we create a new object using the Dog class.
    # The parameters 'name' , 'color' and 'breed' must be used every time we call the Dog class.
    # Since every dog (usually) has a name, is a color, and some kind of breed i will include these in the init method
    # to help me describe the dog. You can consider these three parameters more like 'attributes' of a dog.
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed

    # i can call the following three methods to perform some kind of action with the Dog class.
    def describe(self):
        print(self.name + " is a " + self.color + " " + self.breed + ".")

    def jump(self):
        print(self.name + " just jumped!")

    def sit(self):
        print("Sit, " + self.name + "! Good dog!")

# Below is where i create (or 'instantiate') an object called 'dog1' I supply the name 'fido', the color 'black', and
# the breed 'lab'.


dog1 = Dog("Fido", "black", "lab")


# Here is where i call the dog1 class object and pass it the three methods 'describe' , 'jump', and 'sit'.

dog1.describe()
dog1.jump()
dog1.sit()


'''When i run this script i get the following output:

Fido is a black lab.  <--dog1.describe()
Fido just jumped!  <--dog1.jump()
Sit, Fido! Good dog!  <--dog1.sit()

'''
