"""EX01 - Charlde - A cute step toward Wordle."""
__author__ = "730470511"


"""Creating variables and testing if they contain the correct amounts of characters"""
players_word: str = input("Enter a 5-character word: ")
if len(players_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    players_character: str = input("Enter a single character: ")
    if len(players_character) != 1:
        print("Error: Character must be a single character. ")
        exit()
    else:
        print("Searching for " + players_character + " in " + players_word)


"""Locating where the players input character is in terms of index"""
amount = 0
if players_character == players_word[0]:
    print(players_character + " found at index 0")
    amount = amount + 1
if players_character == players_word[1]:
    print(players_character + " found at index 1")
    amount = amount + 1
if players_character == players_word[2]:
    print(players_character + " found at index 2")
    amount = amount + 1
if players_character == players_word[3]:
    print(players_character + " found at index 3")
    amount = amount + 1
if players_character == players_word[4]:
    print(players_character + " found at index 4")
    amount = amount + 1


"""Represents the number of times the character shows up in the players word"""
if amount == 5:
    print("5 instances of " + players_character + " found in " + players_word)
if amount == 4:
    print("4 instances of " + players_character + " found in " + players_word)
if amount == 3:
    print("3 instances of " + players_character + " found in " + players_word)
if amount == 2:
    print("2 instances of " + players_character + " found in " + players_word)
if amount == 1:
    print("1 instance of " + players_character + " found in " + players_word)
if amount == 0:
    print("No instances of " + players_character + " found in " + players_word)