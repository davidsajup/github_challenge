import random

choices = ('stone','paper','scissors')
emojis = {'stone' : '🪨','paper':'📄','scissors':'✂️'}

while True:

    user_choice = input("Enter your choice (stone/paper/scissors) : ").lower()
    computer_choice = random.choice(choices)

    if user_choice not in choices:
        print("Enter a valid choice!!!")
        continue

    print("You chose",emojis.get(user_choice))
    print("Computer chose",emojis.get(computer_choice))

    if user_choice == computer_choice:
        print("Tied")

    elif ((user_choice == 'stone' and computer_choice == 'scissors') or
          (user_choice == 'scissors' and computer_choice == 'paper') or
          (user_choice == 'paper' and computer_choice == 'stone')):
        print("You won")

    else:
        print("You lost")

    play_again = input("Would you like to play again?(y/n) :")

    if play_again != 'y':
        print("Thanks for playing")
        break


