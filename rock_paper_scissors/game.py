import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_image = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 1 for rock, 2 for paper, 3 for scissors.\n"))

if user_choice >=1 and user_choice <=3:
    print(game_image[user_choice-1])
    
computer_choice = random.randint(1,3)
print(f"Computer Choice: {game_image[computer_choice-1]}")

if user_choice >=4 or user_choice <=0:
    print("You typed invalid input. You lose!")
elif user_choice == 1 and computer_choice == 3:
    print("You win!")
elif computer_choice == 1 and user_choice == 3:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a drow!")