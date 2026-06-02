
import random
while True :
    choice=input("You want to roll dice(y/n): ").lower()

    if choice=="y":
        
        num1=random.randint(1,6)
        num2=random.randint(1,6)
        #print((num1,num2))
        #print(f"{(num1,num2)}")
        
        print(f"({random.randint(1,6)},{random.randint(1,6)})")

    elif choice=="n":
        print("Bye♥!")
        break
        
    else:
        print("Enter y or n.")
