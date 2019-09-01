import time
import random
import sys

NUMBER_OF_TILES = 100
SLEEP_BETWEEN_MOVES = 1
DICE_FACES = 6
CURRENT_PLAYER = 1

# snake & ladders are both dictionaries: takes you down from 'key' to 'value'
snakes = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 63
}

ladders = {
    3: 20,
    6: 14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}

# 0th index for player_name & 1st index for player_current_score
players = [
    [None, 0],
    [None, 0]
]

player_turn_text = [
    "Go.",
    "Please proceed.",
    "Lets win this.",
    "Are you ready?",
    "On to you.",
]

snake_bite = [
    "boohoo",
    "bummer",
    "snake bite",
    "oh no",
    "dang",
    "yikes",
    "uh! oh",
]

ladder_jump = [
    "woohoo",
    "woww",
    "nailed it",
    "oh my God...",
    "yaayyy",
    "hell yeaa",
]

def welcome_msg():
    msg = """
    Welcome {0}, {1} Snake and Ladder Game.
    
    Rules:
      1. Initally both the players are at starting position i.e. 0. 
      2. You climb the ladder if you land at the tail of the ladder.
      3. Snake bite happens if you land at the head of the snake.
      4. The first player to get to the {2} position is the winner.
      5. Hit enter to roll the dice.
    
    """.format(players[0][0], players[1][0], NUMBER_OF_TILES)
    print(msg)

def get_player_names():
    while not players[0][0]:
        players[0][0] = input("Please enter a valid name for first player: ")

    while not players[1][0]:
        players[1][0] = input("Please enter a valid name for second player: ")


def get_dice_value():
    time.sleep(SLEEP_BETWEEN_MOVES)
    dice_value = random.randint(1, DICE_FACES)
    print("Its a " + str(dice_value))
    return dice_value


def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


def check_snake_ladder(player_name, current_value, dice_value):
    time.sleep(SLEEP_BETWEEN_MOVES)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > NUMBER_OF_TILES:
        print("You need " + str(NUMBER_OF_TILES - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value


def check_win(player_name, position):
    time.sleep(SLEEP_BETWEEN_MOVES)
    if NUMBER_OF_TILES == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        sys.exit(1)


def start():
    get_player_names()
    welcome_msg()
    time.sleep(SLEEP_BETWEEN_MOVES)
    time.sleep(SLEEP_BETWEEN_MOVES)
    
    global CURRENT_PLAYER

    while True:
        time.sleep(SLEEP_BETWEEN_MOVES)
        input_1 = input("\n" + players[CURRENT_PLAYER-1][0] + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_value()
        time.sleep(SLEEP_BETWEEN_MOVES)
        print(players[CURRENT_PLAYER-1][0] + " moving....")
        players[CURRENT_PLAYER-1][1] = check_snake_ladder(players[CURRENT_PLAYER-1][0], players[CURRENT_PLAYER-1][1], dice_value)

        check_win(players[CURRENT_PLAYER-1][0], players[CURRENT_PLAYER-1][1])
        
        CURRENT_PLAYER = 2 if CURRENT_PLAYER == 1 else 1


start()