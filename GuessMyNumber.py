import random

print("\tWelcome to 'Guess My Number!'")

# This stores the previous guesses and tells us whether they are right
class oldGuesses(object):
    def __init__(self, low, high):
        # This is the initialization data
        self.guesses = []
        self.low = low
        self.high = high
    
    # This function checks to see the guess isn't in the list and it adds it
    def addNewGuess(self, guess):
        if guess not in self.guesses:
            self.guesses.append(guess)
    
    def checkIfPossible(self, guess):
        # This function checks if the guess is in the range or already in the list
        isPossible = []
        if self.low < guess < self.high:
            isPossible.append(True)
        else:
            isPossible.append(False)
            
        if guess in self.guesses:
            isPossible.append(False)
        else:
            isPossible.append(True)
            self.addNewGuess(guess)
        
        if False in isPossible:
            return False
        else:
            return True

def game():
    # Ask the User the input number
    lowest = int(input("\nWhat do you want the lowest (min) number to be? "))
    highest = int(input("\nWhat do you want the highest (max) number to be? "))
    
    # Telling the User the numbers again
    print("Ok, I'm thinking of a number between ", lowest, " and", highest)
    
    # Creating the new random number and initializing the game
    the_number = random.randint(lowest, highest)
    # I felt it was easier to have this class to check if the guess was possible
    guesses = oldGuesses(lowest, highest)
    tries = 0
    x = True
    while x:
        guess = int(input("\nTake a Guess: "))
        ifPossible = guesses.checkIfPossible(guess)
        if ifPossible:
            tries += 1
            x = False
        else:
            print("Try Again.")
    
    # The while loop until the user gets the right answer
    while guess != the_number:
        # Logic for the Game
        if guess > the_number:
            if highest > guess:
                highest = guess
            # Give the user their hint
            print("\nLower..."
                "\nHint:",lowest, "< x <", highest)

        else:
            if lowest < guess:
                lowest = guess
            # Give the user their hint
            print("\nHigher..."
                "\nHint:",lowest, "< x <", highest)
        
        # Continues the loop
        x = True
        while x:
            guess = int(input("\nTake a Guess: "))
            ifPossible = guesses.checkIfPossible(guess)
            if ifPossible:
                tries += 1
                x = False
            else:
                print("Try Again.")
    
    # Congratulate User and tell them their score
    print("\nYou Guessed It! The number was ", the_number)
    
    # Change the message depending on the score
    if tries < 5:
        print("Nice Job! You did it in ", tries, " tries. Its a high score!")
    else:
        print("You did it in ", tries, " tries")



# Running the Game

game()
response = input("\nPlay Again (y/n)? ").lower()

# While Loop so the game keeps going whenever the player says y or Y
while response == "y":
    game()
    response = input("\nPlay Again (y/n)? ")
    
# Terminating the Program
print("\nThanks for playing!")
input("Enter to Exit")