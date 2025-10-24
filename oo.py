import random

choices = ['heads', 'tails']

user_choice = input('Enter your choice:')
computer_choice = ""
if user_choice == 'heads':
    computer_choice += 'tails'
else:
    computer_choice += 'heads'

toss = random.choice(choices)

if user_choice == toss:
    print(f'computer choice: {computer_choice}')
    print(f"your choice: {user_choice}")
    print(f"you won {toss}")
else:
    print(f'computer choice: {computer_choice}')
    print(f"your choice: {user_choice}")
    print(f"you loss {toss}")
