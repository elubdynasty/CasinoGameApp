from random import randint


def casino_game():


    print("Make a maximum bet. If you win, the number matched will be yours. Goodluck!")
    playerinp_maxnum = input() #The player enters the maxnum. Any range up to the highest one will be picked by the comp
    
    # => Pseudocode
    #There will be a while loop until it matches the player's best bet against the comp. You wanna repeat the bet?
    #There will be limits on guess (4-5)
    #When the player bets higher than the comp's bet, It'll say, 'Make it lower', otherwise 'make it higher

    maxnum_int = int(playerinp_maxnum)

    comp_pick = randint(1, maxnum_int+1)

    #count_wins = 0
    while True:

        print("Make a guess!")
        player_guess = input()

        #if int(player_guess) > maxnum_int and int(player_guess) < 1:

        #print(f'Sorry, enter another valid num between $1 and ${maxnum_int}')

        if int(player_guess) < comp_pick:
            print('Higher')

        elif int(player_guess) >  comp_pick:
            print('Lower')

        elif int(player_guess) ==  comp_pick:
            print('Matched')
            break

        else:
            print('Wrong input. Try again!')


        #still accepts number greater than maximum number


   

casino_game()



