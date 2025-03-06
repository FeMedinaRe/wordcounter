import random

randomNumber = random.randint(1, 100)

while guess != randomNumber:
    guess = int(input("Ingresa el número: "))
    