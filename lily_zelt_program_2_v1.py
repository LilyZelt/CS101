###################################
#CS101 0002
#Program 2: Greedy Coins
#Author:  Lily Zelt
#Email: bzgkd@mail.umkc.edu
###################################

import random

#Prompt user to flip or hold during their turn.
def ask_user_to_flip_or_hold():
    flip_input_from_user = input('Input No to hold pot. Input Yes to keep flipping!')
    while flip_input_from_user not in ('Y', 'y', 'Yes', 'yes', 'N', 'n', 'No', 'no'):
        flip_input_from_user = input('You must enter [No] or [Yes] to continue.')
    if flip_input_from_user in ('Y', 'y', 'Yes', 'yes'):
        flipping = True
    else:
        flipping = False
    return flipping

#Converts 1s and 0s to heads and tails for user.
def make_flip_easy_to_read(coin1, coin2, coin3):
    if coin1 == 0:
          coin1str = 'Tails'
    else:
          coin1str = 'Heads'
    if coin2 == 0:
          coin2str = 'Tails'
    else:
          coin2str = 'Heads'
    if coin3 == 0:
          coin3str = 'Tails'
    else:
          coin3str = 'Heads'
    return (coin1str, coin2str, coin3str)

#FIXME values put in to program wouldn't crash during testing.
pot = 0
user_score = 2
ai_score = 4
turn = 'User'


#Player Turn Sequence
flipping = True
while flipping == True:
    print('Pot Value: %d. User Score: %d. AI Score: %d. It is the %s\'s turn.' % (pot, user_score, ai_score, turn))
    #Telling the AI what to do.
    if turn == 'AI' and pot < 8:
        if ai_score >= 20:
            flipping = False
        else:
            flipping = True
    elif turn == 'AI' and pot >= 8:
        flipping = False
    #Otherwise, ask the user what to do.
    else:
        flipping = ask_user_to_flip_or_hold()
    #Player holds.
    if flipping == False:
        if turn == 'AI':
            ai_score += pot
        else:
            user_score += pot
        pot = 0
        print('Giving the coins to the other player. FIXME actually change the turn!')
        #FIXME how to make turns go from user to ai and ai to user? -- change_turn = True
    #Player Flips
    if flipping == True:
        #flip 3 coins.
        coin1 = random.randint(0,1)
        coin2 = random.randint(0,1)
        coin3 = random.randint(0,1)
        #Make flips easier for user to read & output flip results.
        print('Coin values after flip: %s %s %s' % (make_flip_easy_to_read(coin1, coin2, coin3)))
        #Busting on three tails, resetting pot, and changing turns.
        if coin1 == coin2 == coin3 == 0:
            print('Nooo! FIXME change turn to other player')
            pot = 0
            #FIXME change turns!
        #Increasing pot and continuing to play at top of loop.
        else:
            pot += coin1 + coin2 + coin3
    #How to say which player's score increases!???
    #After the turn here's what happens.
    #FIXME include getting out of this loop, changing next game's first player.
    if ai_score >= 20:
        print('AI wins with %d coins!' % ai_score)
    if user_score >= 20:
        print('You win with %d coins!' % user_score)






