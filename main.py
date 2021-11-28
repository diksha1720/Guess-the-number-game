import art
import random

print(art.logo)
actual_number=random.randint(1,101)


def guess_number(attempts):
  if(attempts):
    print(f"\nYou have {attempts} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess==actual_number:
      # print(art.win)
      print("\nCongrats!!!! You guessed the correct answer.You win")
      return 
    elif guess>actual_number:
      print("\nNumber guessed too high")
    elif guess<actual_number:
      print("\nNumber guessed too low")
    attempts-=1
    guess_number(attempts)
  else:
    # print(art.lose)
    print("\nYou lose")
    print(f"\nThe correct number was {actual_number}")

def start():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100\n")
  difficulty_level=input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty_level=='hard':
    no_of_attempts=5
  elif difficulty_level=='easy':
    no_of_attempts=10
  else:
    print("Wrong choice")
    return
  guess_number(no_of_attempts)


start()