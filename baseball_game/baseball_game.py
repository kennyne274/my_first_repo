# Baseball Game (Number Baseball / Bulls and Cows)
# Guess the 3-digit secret number

import random

def generate_number():
    """Generate a 3-digit number with unique digits from 1 to 9 (no zero)"""
    return random.sample(range(1, 10), 3)


def get_user_guess():
    """Get and validate user's 3-digit guess"""
    while True:
        s = input("Enter a 3-digit number: ").strip()
        
        if s.lower() == 'q':
            return None

        # Validation: must be exactly 3 digits, no duplicates, no zero
        if len(s) != 3 or not s.isdigit() or len(set(s)) < 3 or '0' in s:     
            print("Please enter 3 different digits (1-9, no duplicates, no zero).")
            continue

        guess = [int(x) for x in s]
        return guess


def calculate_score(guess, target):
    """Calculate strikes and balls"""
    strikes = 0
    balls = 0

    for i in range(3):
        if guess[i] == target[i]:
            strikes += 1
        elif guess[i] in target:
            balls += 1

    return strikes, balls


def main():
    target = generate_number()
    chances = 5

    print("=" * 50)
    print("BASEBALL GAME START")
    print("You have 5 chances.")
    print("Each 'OUT' reduces your remaining chances by 1.")
    print("Guess a 3-digit number using digits 1-9 (no duplicates, no zero)")
    print("=" * 50)

    while chances > 0:
        guess = get_user_guess()
        if guess is None:
            print("Game exited by user.")
            return

        strikes, balls = calculate_score(guess, target)

        if strikes == 3:
            print(f"Congratulations! You got it right! The answer was {target}")
            break
        elif strikes == 0 and balls == 0:
            print(f"OUT! Remaining chances: {chances}")
            chances -= 1
        else:
            print(f"{strikes} Strike(s), {balls} Ball(s)")

    else:
        print(f"Game Over! The correct answer was {target}.\nBetter luck next time!")


if __name__ == "__main__":
    main()
