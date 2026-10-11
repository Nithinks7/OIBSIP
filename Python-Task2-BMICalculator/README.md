[README.md](https://github.com/user-attachments/files/33295382/README.md)
# BMI Calculator (Beginner Tier)

**Oasis Infobyte SIP | Python Programming Track | Task 2**

A command-line Python program that calculates Body Mass Index (BMI) and
classifies the result into a health category.

## Features
- Prompts for weight (kg) and height (m)
- Calculates BMI using `BMI = weight / (height²)`
- Shows BMI rounded to 2 decimal places and the category
- Input validation: rejects text, empty input, zero and negative values
- Catches likely centimetre input (height over 3 m)
- Option to calculate again without restarting

## BMI Categories
| BMI | Category |
|-----|----------|
| < 18.5 | Underweight |
| 18.5 – 24.9 | Normal weight |
| 25 – 29.9 | Overweight |
| ≥ 30 | Obese |

## How to Run
Requires Python 3.6+ (no external libraries).

```bash
python bmi_calculator.py
```

## Sample Output
```
Enter your weight in kg (e.g. 70): 70
Enter your height in metres (e.g. 1.75): 1.75

--- Result ---
Your BMI is: 22.86
Category   : Normal weight
--------------
```

## Tech Used
Python 3, built-in `input()` and basic arithmetic.

## Note
BMI is a general screening measure and not a medical diagnosis.

## Author
Nithin K S - https://github.com/Nithinks7
