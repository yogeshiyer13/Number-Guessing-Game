# Number Guess Game

import random


def gameNumber():

    while True:
        difficulty = input("Type: E, M, H for easy, medium, or hard number range:\n").lower()    

        if difficulty == 'e':
            return random.randint(0,20)

        elif difficulty == 'm':
            return random.randint(0,50)

        elif difficulty == 'h':
            return random.randint(0,100)

        else:
            print("Incorrect input")


def numberGuessGame():
    number = gameNumber()
    while True:        
        try:  
           guess = int(input("Your guess: "))
           if number == guess:
               print("Correct guess!\n")
               return numberGuessGame() if input("play again?(y/any key to exit) ").lower() == 'y' else 0
           print("Too High" if number < guess else "Too Low")            
        except ValueError:
            print("must be an integer value\n")


def main():
    numberGuessGame()

if __name__ == '__main__':
    main()
