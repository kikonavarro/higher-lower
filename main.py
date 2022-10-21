from game_data import data
from art import logo, vs
import random


keep_playing = True
score = 0
print(logo)

while keep_playing:

    first_player = random.choice(data)
    second_player = random.choice(data)

    if first_player == second_player:
        second_player = random.choice(data)

    print(f'Player A is {first_player["name"]}')
    print(vs)
    print(f'Player B is {second_player["name"]}\n')

    selected_player = (
        input("Who has more followers? Type 'A' or 'B': ").lower())

    if first_player['follower_count'] > second_player['follower_count']:
        winner = 'a'
        second_player = random.choice(data)
    else:
        winner = 'b'
        first_player = second_player

    if winner == selected_player:
        score += 1
        print(f'you win, your score is {score}, try again \n')

    else:
        print(f'you loose, your final score is {score}')
        keep_playing = False
