import random


def play():
    possibleAction = ['R', 'P', 'S']
    user = input("Pick a weapon:\n 'R' for rock,\n 'P' for paper,\n 'S' for scissors", ).capitalize()
    computer = random.choice(possibleAction)

    # for item in possibleAction:
    #     if user not in possibleAction:
    #         user = input(" Error, invalid input! Pick a weapon: 'R' for rock, 'P' for paper, 'S' for scissors", ).capitalize()
    
    while user not in possibleAction:
        user = input(" Error, invalid input! Pick a weapon: 'R' for rock, 'P' for paper, 'S' for scissors", ).capitalize()
    
    def win(player, opponent):
        if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
            return True

    print(f'Player ({user}) : CPU ({computer})')

    if user == computer:
        print('Oops! It\'s a tie')
        print('Let\'s play again') 
        play() 

    if win(user, computer):
        print('You are the winner, Player wins')

    else: print('You lost, Computer wins') 




play()
       