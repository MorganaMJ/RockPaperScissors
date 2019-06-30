import random


WHO_BEATS_WHO = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}


def pc_random():
    rps = ['rock', 'paper', 'scissors']
    index = random.randint(0, 2)
    return rps[index]


def game(pc_score, player_score):
    player = input('Pick rock, paper or scissors:')
    pc_pick = pc_random()

    if WHO_BEATS_WHO[player] == pc_pick:
        player_score += 1
    elif WHO_BEATS_WHO[pc_pick] == player:
        pc_score += 1
    print(f'PC:{pc_pick} Player:{player}')
    print('scoreboard:\n player score :{}\n pc score :{}'.format(player_score, pc_score))
    next_game = input('Do you wanna play again?')
    next_game.strip().lower()
    if next_game == 'yes':
        game(pc_score, player_score)
    elif next_game == 'no':
        exit()


game(0, 0)





