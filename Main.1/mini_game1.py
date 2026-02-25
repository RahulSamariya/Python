"""We all have played snake, water gun game in our childhood. If you havent, google the
rules of this game and write a python program capable of playing this game with the user"""

import random

computer = random.choice([-1 , 1, 0])
user = input("Enter s for Snake, w for Water, g for Gun: ")
your_dict = {"s": 1, "w": -1, "g" : 0 }
you = your_dict[user]

if (computer == you ):
    print("It's Draw")

elif(computer == 1 and you == 0):
    print("you lose")

elif(computer == 1 and you == -1):
    print("you Win")

elif(computer == 0 and you == -1):
    print("you lose")

elif(computer == 0 and you == 1):
    print("you Win")

elif(computer == -1 and you == 1):
    print("you lose")

elif(computer == -1 and you == 0):
    print("you Win")

