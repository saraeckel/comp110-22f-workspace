"""Wordle!"""

__author__ = "730470511"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    secret_term: str = "codes"
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret_term))
        print(emojified(guess, secret_term))
        if guess == secret_term and turns <= 6:
            print(f"You won in {turns}/6 turns!")
            return
        elif guess != secret_term and turns >= 6:
            print("X/6 - Sorry, try again tomorrow!")
            return
        turns += 1


def contains_char(term: str, single_letter: str) -> bool:
    """Searching for a single letter in and throughout the term."""
    assert len(single_letter) == 1
    i: int = 0
    while i < len(term):
        if single_letter == term[i]:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Testing letters to determine if they produce a green, yellow, or white box in a string of emojis."""
    assert len(guess) == len(secret)
    emojis_printed: str = ""
    idx = 0 
    white: str = "\U00002B1C"
    green: str = "\U0001F7E9"
    yellow: str = "\U0001F7E8"
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            emojis_printed += green
        elif contains_char(secret, guess[idx]) is True:
            emojis_printed += yellow
        else:
            emojis_printed += white
        idx += 1
    return emojis_printed


def input_guess(expected_length: int) -> str:
    """Ask user for a guess and continue until the provided input is of expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


if __name__ == "__main__":
    main()