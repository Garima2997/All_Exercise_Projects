ans = 20
guess = 5

while guess != 0:
    num = int(input("Guess the number: "))
    if num < ans:
        print("Wrong Number. Guess the higher number!")
        print(f"You have {guess -1} attempts left")
    elif num > ans:
        print(f"Wrong Number. Guess the lower number!")
        print(f"You have {guess -1} attempts left")
    else:
        print(f"Bingo!! You Won!! in {guess} attempts.")
        break
    guess -= 1
if(guess == 0):
    print("Game Over!")

