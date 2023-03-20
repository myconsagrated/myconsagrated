from player import Player
import random


def start_battle():
    player = Player()
    opponent = Player()

    running = True

    while running:
        player.action = choose_action(player)
        opponent.action = get_input_from_opponent_and_update(opponent)

        running = execute_actions(player, opponent)


def choose_action(player: Player):
    """ """

    input_msg = """
        --> Escolha uma ação: 
        (1) Recarregar 
        (2) Defender 
        (3) Atirar
    """

    input_ = input(input_msg)
    action_dict = {
        "1": player._add_ammo,
        "2": print,
        "3": player._update_ammo_from_shot,
    }

    try:
        action_dict[input_]()
    except:
        while input_ == "3":
            print("not enough bullets, pick another action")
            input_ = input(input_msg)
        action_dict[input_]()

    return input_


def get_input_from_opponent_and_update(opponent: Player):
    input_ = random.choice(["1", "2", "3"])

    action_dict = {
        "1": opponent._add_ammo,
        "2": print,
        "3": opponent._update_ammo_from_shot,
    }

    try:
        action_dict[input_]()
    except:
        print("not enough bullets, pick another action")
        input_ = random.choice(["1", "2"])
        action_dict[input_]()

    return input_


def execute_actions(player: Player, opponent: Player):
    print(
        f""" 
        Player action = {player.action}
        Opponent action = {opponent.action}

        P ammo: {player.ammo}
        O ammo: {opponent.ammo}
    """
    )

    if player.action == "1" and opponent.action == "3":
        print("Opponent Wins")
        return False

    elif opponent.action == "1" and player.action == "3":
        print("Player Wins")
        return False

    return True
