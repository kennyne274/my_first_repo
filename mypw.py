import random
import string

def generate_password(length):
    """
    Function to generate a random password
    :param length: password length
    :return: generated password
    """
    if length < 6:
        raise ValueError("Password must be at least 6 characters long.")

    # Password components
    letters = string.ascii_letters   # Uppercase and lowercase alphabets
    digits = string.digits           # Numbers
    symbols = string.punctuation     # Special characters

    # Mandatory components (one letter, one digit, one symbol)
    mandatory = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Remaining characters
    all_characters = letters + digits + symbols  # Letters + digits + symbols
    random_part = random.choices(all_characters, k=length - len(mandatory))

    # Combine mandatory + random and shuffle
    password_list = mandatory + random_part
    random.shuffle(password_list)

    return ''.join(password_list)

# Main function execution area
def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter password length (minimum 6): "))
        num = int(input("Enter number of passwords to generate: "))

        print("\n=== Generated Passwords ===")
        for i in range(num):
            pw = generate_password(length)
            print(f"{i+1}. {pw}")

    except ValueError as e:
        print(f"Error: {e}")

# Program execution
if __name__ == "__main__":
    main()


# Example Output
# 1. (r%.D7Ug/{Op
# 2. b(r[DZl;%35r
# 3. uEjH8s>3v}"3