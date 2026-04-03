# Dice Rolling Game
# User VS Computer

import random
import time


dice_drawing = {
        1: [
            "+-------+",
            "|       |",
            "|   ●   |",
            "|       |",
            "+-------+"
        ],
        2: [
            "+-------+",
            "| ●     |",
            "|       |",
            "|     ● |",
            "+-------+"
        ],
        3: [
            "+-------+",
            "| ●     |",
            "|   ●   |",
            "|     ● |",
            "+-------+"
        ],
        4: [
            "+-------+",
            "| ●   ● |",
            "|       |",
            "| ●   ● |",
            "+-------+"
        ],
        5: [
            "+-------+",
            "| ●   ● |",
            "|   ●   |",
            "| ●   ● |",
            "+-------+"
        ],
        6: [
            "+-------+",
            "| ●   ● |",
            "| ●   ● |",
            "| ●   ● |",
            "+-------+"
        ]
    }


# Roll the dice
def roll_dice():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    return num1, num2


# Print dice faces side by side
def print_dice(d1, d2, dice_drawing):
    for i1, i2 in zip(dice_drawing[d1], dice_drawing[d2]):
        print(i1 + "     " + i2)


def main():
    user_score = 0
    computer_score = 0

    # Game loop
    while True:
        
        user_input = input("Roll the dice? (y/n) : ").lower().strip()

        if not user_input:
            print("You didn't enter anything.")
            continue

        elif user_input == 'y':
            # User rolls
            num1, num2 = roll_dice()
            user_score += num1 + num2

            # Computer rolls
            com_num1, com_num2 = roll_dice()
            computer_score += com_num1 + com_num2

            print("\nYou rolled the dice.")
            print_dice(num1, num2, dice_drawing)
            print(f"Your 🎲 Current Score : {user_score}\n")

            time.sleep(1)  # 1 second pause for better UX

            print("The computer rolled the dice.")
            print_dice(com_num1, com_num2, dice_drawing)
            print(f"Computer's 🎲 Current Score : {computer_score}\n")

        elif user_input == 'n':
            print("Game ended. Goodbye!")
            break

        else:
            print("Please enter (y/n)")

        # Check if anyone reached 20 points or more
        if user_score >= 20 or computer_score >= 20:
            if user_score > computer_score:
                print("You Win! Computer Loses.")
            elif user_score < computer_score:
                print("Computer Wins! You Lose.")
            else:
                print("It's a Draw 🤝")

            break


# Game Start Screen
print("=" * 40)
print("🎲 DICE GAME START 🎲")
print("Roll the dice and reach 20 points first to win!")
print("=" * 40)

main()
