import random

random=random.randint(1,101)
count=0
print(random)
while True:
    try:
        num=int(input("Enter a Number 1-100: "))
        count+=1
    except ValueError:
        print("Enter Valid Number")

    if num>random:
        print("Too High")
    elif num<random:
        print("Too Low")
    else:
        print(f"Congratulation ! No is {random}")
        print(f'You guessed in {count} attempt ')
        break