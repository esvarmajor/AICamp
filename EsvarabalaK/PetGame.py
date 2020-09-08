import pygame
from MyDog import MyDog


class PetGame:

    def main():
        a_dog = MyDog("Rover", 6)
        a_dog.bark()
        a_dog.spend_time(100)

    if __name__ == "__main__":
        main()