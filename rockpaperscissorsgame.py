import random

print('Welcome to the game of Rock Paper Scissors!')
print('rock / paper / scissors')

user_input = input('Enter rock paper scissors: ')

choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)

print("Computer chose:", computer)

if user_input == computer:
    print("It's a draw!")

elif (user_input == 'rock' and computer == 'scissors') or \
     (user_input == 'paper' and computer == 'rock') or \
     (user_input == 'scissors' and computer == 'paper'):
    print("You win!")

else:
    print("You lose!")
