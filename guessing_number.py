import random

secret_number = random.randint(1, 100)
count = 0

while True:
    try:
        num = int(input("Enter a number (1-100): "))
        count += 1
    except ValueError:
        print("Please enter a valid number.")
        continue

    if num > secret_number:
        print("Too High")
    elif num < secret_number:
        print("Too Low")
    else:
        print(f"Congratulations ♥ The number was {secret_number}")
        print(f"You guessed it in {count} attempts.")
        break