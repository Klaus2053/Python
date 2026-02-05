# coding=utf-8
# Erstellt von Klaus Barth Rochol
import random
# random module is a built-in module to generate pseudo-random variables
def display_gameplay():
    """
    Displays the gameplay
    : return: None
    """
    print('\nWillkommen zum Zahlenratespiel!')
    print('In diesem Spiel hast du nur 7 Versuche, um eine Zahl zwischen 1 und 10 zu erraten')
    print('Hinweis: gib \'beenden\' ein, um das Spiel zu beenden')
def startGame():
    """
    Gets user response to start or end the game
    : return: str
    """
    # call the function to display gameplay
    displayGameplay = display_gameplay()
    # make a list of the possible inputs
    # to start or end the game
    possible_responses = ['J','JA','N','NEIN','BEENDEN']
    # get user's response
    user_response = input('\nSpiel starten? (ja/nein): ').strip().upper()
    while user_response not in possible_responses:
        print('\nUngültige Eingabe!')
        user_response = input('\nSpiel starten? (ja/nein): ').strip().upper()
    else: return user_response
def game():
    """
    Controls the game
    : return: None
    """
    # call the function to get user's response
    play_game = startGame()
    # assign the number of trials the user has to a variable
    number_of_trials = 7
    # initialise new_game to true
    new_game = True
    while play_game == 'JA' or play_game == 'J':
        # make a list that contains all the
        # numbers a user can guess
        accepted_number_picks = [str(i) for i in range(1,11)]
        # get user's number
        user_input = input('\nErrate eine Zahl zwischen 1 und 10: ').strip().upper()
        while user_input not in accepted_number_picks and user_input != 'BEENDEN' :
            print('Ungültige Eingabe!')
            user_input = input('\nErrate eine gültige Zahl zwischen 1 und 10: ').strip().upper()
        if user_input == 'BEENDEN':
            print('Tschüss Spieler!')
            break
        else:
            # generate a random number in the range 1-10
            # and assign it to a variable
            # check if new_game, if true generate new computer_number else don't
            if new_game:
                computer_number = random.randint(1,10)
                new_game = False
            user_input = int(user_input)
            if user_input < computer_number:
                number_of_trials -= 1
                print(f'Hoppla, {user_input} ist zu niedrig')
                if number_of_trials != 0:
                    print(f'Du hast noch {number_of_trials} Versuch(e) übrig')
                    play_game = input('\nNochmal raten? (ja/nein): ').strip().upper()
                else:
                    print('\nSpiel vorbei! Du hast 0 Versuche übrig...versuch es beim nächsten Mal härter 😉')
                    break
            elif user_input > computer_number:
                number_of_trials -= 1
                print(f'Hoppla, {user_input} ist zu hoch')
                if number_of_trials != 0:
                    print(f'Du hast noch {number_of_trials} Versuch(e) übrig')
                    play_game = input('\nNochmal raten? (ja/nein): ').strip().upper()
                else:
                    print('\nSpiel vorbei! Du hast 0 Versuche übrig...versuch es beim nächsten Mal härter 😉')
                    break
            elif user_input == computer_number:
                number_of_trials -= 1
                print(f'Glückwunsch!!..du hast richtig geraten, nach {7 - number_of_trials} Versuch(en)')
                play_game = input('\nMöchtest du nochmal spielen? (ja/nein): ').strip().upper()
                # if the user wishes to play again, assign
                # the number of trials the user has to a variable
                number_of_trials = 7
                # start a new game
                new_game = True
game()