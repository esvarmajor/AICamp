class MyPet:

    def __init__(self, name):
        self.name = name
        self.trust=0

    def pet(self):
        print("Your pet " + self.name + " seemed happy that you pet them.")

    def make_noise(self):
        print("Noise noise noise.")

    def spend_time(self,minutes_spent):
        self.trust=minutes_spent


orange_cat = MyPet("Miles")
small_dog = MyPet("Fido")

print(orange_cat.name)
small_dog.pet()


class MyDog(MyPet):

    def bark(self):
        print("Woof woof woof")


my_dog = MyDog("Spike")
my_dog.pet()
my_dog.bark()