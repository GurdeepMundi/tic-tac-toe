import time
import os


def draw_table(table):
    """This function will print the table on the screen"""
    vl = ' | '  # vertical Line
    hl = '__________'  # horizontal line
    print(table[1] + vl + table[2] + vl + table[3])
    print(hl)
    print(table[4] + vl + table[5] + vl + table[6])
    print(hl)
    print(table[7] + vl + table[8] + vl + table[9])
    print("")


def is_empty(address):
    """Checks if a position in the table is empty"""
    return True if table[address] == ' ' else False


def play_again():
    """Ask the user if wants to play the game again.
    Returns true if user wants to play.
    """
    global keep_playing
    p = 'z'
    p = input("do you want to play again? (Y or N): ")
    while p.upper() != 'Y' and p.upper() != 'N':
        p = input("please enter the right input (Y or N): ")
    keep_playing = True if p.upper() == 'Y' else False


def insert_symbol(symbol, address):
    """To put a symbol on the table if there is no winner"""
    if is_empty(address):
        table[address] = symbol
        draw_table(table)
        if game_is_over():
            global found_winner
            if symbol == 'X':
                print("You lost this game, better luck next time.")
            else:
                print("Player wins!")
            found_winner = True
            # Ask if player wants to play again
            play_again()
        if is_draw():
            print("You played as good as AI, Cheers!")
            found_winner = True
            # Ask if player wants to play again
            play_again()
        return
    # if position already used
    else:
        address = int(input
                      ("Oops! already occupied, enter another position:  "))
        insert_symbol(symbol, address)
        return


def game_is_over():
    """Check if there is any winner"""
    if table[1] == table[2] == table[3] and table[1] != ' ':
        return True
    elif table[4] == table[5] == table[6] and table[4] != ' ':
        return True
    elif table[7] == table[8] == table[9] and table[7] != ' ':
        return True
    elif table[1] == table[4] == table[7] and table[1] != ' ':
        return True
    elif table[2] == table[5] == table[8] and table[2] != ' ':
        return True
    elif table[3] == table[6] == table[9] and table[3] != ' ':
        return True
    elif table[1] == table[5] == table[9] and table[1] != ' ':
        return True
    elif table[7] == table[5] == table[3] and table[7] != ' ':
        return True
    else:
        return False


def is_it_winner(letter):
    """Returns true if a player the player is winner.

    keyword arguments:
    letter -- e.g. 'O' The symbol of player who you want to check for
     win status.
    """
    if table[1] == table[2] == table[3] and table[1] == letter:
        return True
    elif table[4] == table[5] == table[6] and table[4] == letter:
        return True
    elif table[7] == table[8] == table[9] and table[7] == letter:
        return True
    elif table[1] == table[4] == table[7] and table[1] == letter:
        return True
    elif table[2] == table[5] == table[8] and table[2] == letter:
        return True
    elif table[3] == table[6] == table[9] and table[3] == letter:
        return True
    elif table[1] == table[5] == table[9] and table[1] == letter:
        return True
    elif table[7] == table[5] == table[3] and table[7] == letter:
        return True
    else:
        return False

def is_draw():
    """Returns True if the game was draw, False otherwise"""
    for i in table.keys():
        if table[i] == ' ':
            return False
    return True


def player_turn():
    """Human player's turn"""
    if found_winner:
        initialize_game(keep_playing)
    else:
        print("your turn")
        address = int(input("Please enter your move (1-9):  "))
        insert_symbol(player, address)
    return


def ai_turn():
    """Computer player's turn, uses algorithm"""
    best_score = -1000
    best_address = 0
    for key in table.keys():
        if table[key] == ' ':
            table[key] = ai
            score = algorithm(table, 0, False, -1000, 1000)
            table[key] = ' '
            if score > best_score:
                best_score = score
                best_address = key
    os.system('clear')
    draw_table(table)
    print("AI's Turn")
    time.sleep(1)
    os.system('clear')
    insert_symbol(ai, best_address)
    return


def algorithm(table, depth, is_max, alpha, beta):
    """
    Algorithm to decide which box to choose for next step.

    This algorithm is implementation of minimax algorithm combined with
    alpha-beta pruning to improve decision time.
    :param table: Current state of the game table.
    :param depth: Current depth in the decision tree.
    :param is_max: Type of optimizer, minimizer or maximizer
    :param alpha: The current value of alpha
    :param beta: The current value of beta
    :return: A score, to help making the decision. Higher the better.
    """
    if is_it_winner(ai):
        return 1
    elif is_it_winner(player):
        return -1
    elif is_draw():
        return 0
    if is_max:
        best_score = -2000
        for key in table.keys():
            if table[key] == ' ':
                table[key] = ai
                score = algorithm(table, depth+1, False, alpha, beta)
                table[key] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = 2000
        for key in table.keys():
            if table[key] == ' ':
                table[key] = player
                score = algorithm(table, depth+1, True, alpha, beta)
                table[key] = ' '
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score


def initialize_game(want_another_round):
    """This function shows a welcome message and resets the table to a new
    state

    :param want_another_round: Input from the user stating if want to play the
    game again
    :return:
    """
    if want_another_round:
        vl = ' | '  # vertical Line
        hl = '_____________'  # horizontal line
        global table
        global found_winner
        table = {1: ' ', 2: ' ', 3: ' ',
                 4: ' ', 5: ' ', 6: ' ',
                 7: ' ', 8: ' ', 9: ' '}
        os.system('clear')
        print("Welcome to Tic-Tac-Toe, AI will take the first turn")
        print("Positions on the table are as follows:")
        print(1, vl, 2, vl, 3)
        print(hl)
        print(4, vl, 5, vl, 6)
        print(hl)
        print(7, vl, 8, vl, 9)
        print("\n")
        found_winner = False
        draw_table(table)
        temp = input("press any key to start the game: ")
    else:
        exit()


keep_playing = True
found_winner = False
player = 'O'
ai = 'X'
table = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
initialize_game(True);
while not found_winner:
    ai_turn()
    player_turn()
