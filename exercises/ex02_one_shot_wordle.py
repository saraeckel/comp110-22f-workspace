"""Creating Code for Wordle!"""
__author__ = "730470511"


"""Establishing Secret Word and Asking User for a Guess"""


secret = "python"
guess: str = input("What is your 6-letter guess? ")
while len(guess) != len(secret):
    guess = input("That was not 6 letters! Try again: ") 

"""Checking Indices for Correct Matches!"""
i = 0
emoji_guess = ""
white: str = "\U00002B1C"
green: str = "\U0001F7E9"
yellow: str = "\U0001F7E8"
while i < len(guess):
    # guessed character is in the correct spot
    if guess[i] == secret[i]:
        emoji_guess = emoji_guess + green
    else:
        elsewhere: bool = True
        idx = 0 
        while elsewhere and idx < len(secret):
            if secret[idx] == guess[i]:
                elsewhere = False
            else:
                idx += 1
        if elsewhere is False:
            emoji_guess = emoji_guess + yellow
        else:
            emoji_guess = emoji_guess + white
            
    i += 1
print(emoji_guess)

"""Telling User If They Guessed the Secret or Play Again!"""
if guess != secret:
    print("Not quite. Play again soon! ")
else:
    print("Woo! You got it! ")