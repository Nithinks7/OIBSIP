# Random Password Generator (Beginner Tier)

**Oasis Infobyte SIP | Python Programming Track | Task 3**

A command-line Python tool that generates strong random passwords based on
user-chosen length and character types.

## Features
- Asks for password length (minimum 8 characters enforced)
- Asks which character types to include: uppercase, lowercase, numbers, symbols
- At least 2 character types must be selected
- Guarantees at least one character from every selected type
- Input validation for invalid lengths, non-numeric input and bad choices
- Generate another password without restarting the program

## How to Run
Requires Python 3.6+ (no external libraries).

```bash
python password_generator.py
```

On Mac/Linux use `python3 password_generator.py`.

## Sample Output
```
Enter password length (minimum 8): 12

Choose the character types to include:
  Include uppercase letters (A-Z)? (y/n): y
  Include lowercase letters (a-z)? (y/n): y
  Include numbers (0-9)? (y/n): y
  Include symbols (!@#$...)? (y/n): n

Your generated password:
  k7Tq2mWz9xBe
```

## How It Works
1. One random character is picked from each selected type, so every chosen
   type appears at least once.
2. The remaining characters are picked from all selected types combined.
3. The list is shuffled so the guaranteed characters are not in a fixed position.

Randomness comes from `random.SystemRandom()`, which uses the operating
system's secure random source and is safer for passwords than the default
`random` generator.

## Tech Used
Python 3, `random`, `string`

## Security Note
Generated passwords are only printed to the screen. They are never saved to a file.

## Author
Nithin K S - https://github.com/Nithinks7
