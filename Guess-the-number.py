import random

def main():
    while True:
        x = random.randint(1, 10)

        choice = int(input("Enter your number: "))

        if x == choice:
            print("You guessed the correct number!")
        elif choice < 1 or choice > 10:
            print("The number should be bigger than 0")
        else:
            print("Try again!")
    
    
    
if __name__ == "__main__":
    main()