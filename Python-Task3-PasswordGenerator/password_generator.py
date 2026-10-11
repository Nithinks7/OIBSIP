"""
Random Password Generator (Beginner Tier)
Oasis Infobyte SIP - Python Programming Track - Task 3

Generates a random password based on the length and character types
chosen by the user. Minimum length is 8 and at least 2 character types
must be selected. The password always contains at least one character
from every selected type.
"""

import random
import string

MIN_LENGTH = 8
MAX_LENGTH = 128

# SystemRandom uses the operating system's secure random source,
# which is safer for passwords than the default random generator.
rng = random.SystemRandom()


def get_length():
    """Ask for password length until a valid number is given."""
    while True:
        raw = input(f"Enter password length (minimum {MIN_LENGTH}): ").strip()
        try:
            length = int(raw)
        except ValueError:
            print("  Error: please enter a whole number (e.g. 12).")
            continue
        if length < MIN_LENGTH:
            print(f"  Error: password must be at least {MIN_LENGTH} characters.")
            continue
        if length > MAX_LENGTH:
            print(f"  Error: password cannot be longer than {MAX_LENGTH} characters.")
            continue
        return length


def ask_yes_no(question):
    """Ask a yes/no question and return True for yes."""
    while True:
        answer = input(question + " (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("  Error: please type y or n.")


def get_character_sets():
    """Ask which character types to include. At least 2 are required."""
    options = [
        ("uppercase letters (A-Z)", string.ascii_uppercase),
        ("lowercase letters (a-z)", string.ascii_lowercase),
        ("numbers (0-9)", string.digits),
        ("symbols (!@#$...)", string.punctuation),
    ]
    while True:
        print("\nChoose the character types to include:")
        selected = []
        for name, chars in options:
            if ask_yes_no(f"  Include {name}?"):
                selected.append(chars)
        if len(selected) < 2:
            print("  Error: select at least 2 character types. Try again.")
            continue
        return selected


def generate_password(length, char_sets):
    """Build a password containing at least one char from each selected set."""
    # One guaranteed character from every selected type
    password = [rng.choice(chars) for chars in char_sets]

    # Fill the remaining length from all selected characters combined
    all_chars = "".join(char_sets)
    password += [rng.choice(all_chars) for _ in range(length - len(password))]

    # Shuffle so the guaranteed characters are not always at the start
    rng.shuffle(password)
    return "".join(password)


def main():
    print("=" * 36)
    print("     RANDOM PASSWORD GENERATOR")
    print("=" * 36)

    length = get_length()
    char_sets = get_character_sets()

    while True:
        password = generate_password(length, char_sets)
        print("\nYour generated password:")
        print(f"  {password}\n")

        if not ask_yes_no("Generate another password with the same settings?"):
            break

    print("Thank you for using the Password Generator. Stay safe online!")


if __name__ == "__main__":
    main()

