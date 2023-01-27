from gisim.agent import AttackOnlyAgent, NoAttackAgent  # noqa: E402
from gisim.classes.enums import GameStatus, PlayerID  # noqa: E402
from gisim.game import Game  # noqa: E402

if __name__ == "__main__":
    # player1_deck = {"characters": ["宵宫", "神里绫华", "重云"], "cards": []}
    # player2_deck = {"characters": ["菲谢尔", "柯莱", "香菱"], "cards": []}
    # player1_deck = {
    #     "characters": ["Yoimiya", "Kamisato Ayaka", "Chongyun"],
    #     "cards": [],
    # }
    # player2_deck = {"characters": ["Fischl", "Collei", "Xiangling"], "cards": []}
    player1_deck = {
        "characters": ["Kamisato Ayaka", "Kamisato Ayaka", "Kamisato Ayaka"],
        "cards": [],
    }
    player2_deck = {
        "characters": ["Kamisato Ayaka", "Kamisato Ayaka", "Kamisato Ayaka"],
        "cards": [],
    }
    game = Game(player1_deck, player2_deck, seed=10)
    player1_agent = AttackOnlyAgent(PlayerID.PLAYER1)
    player2_agent = NoAttackAgent(PlayerID.PLAYER2)
    game_end = False
    game_info = game.encode_game_info(PlayerID.SPECTATOR)

    winner = PlayerID.SPECTATOR
    action_cnt = 0
    game_round = 0
    while True:
        if game_round != game_info.round_num:
            game_round = game_info.round_num
            print(f"\n-------------- Round {game_round} --------------\n")
        action_cnt += 1
        active_player = game_info.active_player
        ch = None
        ch_status_list = []

        if active_player == PlayerID.PLAYER1:
            action = player1_agent.take_action(game_info)
        else:
            action = player2_agent.take_action(game_info)

        if active_player == PlayerID.PLAYER1:
            if game_info.player1.dice_zone:
                dice = [str(die) for die in game_info.player1.dice_zone]
            else:
                dice = []
            pos = game_info.player1.active_character_position
            if pos.value is not None:
                ch = game_info.player1.characters[pos.value].character
                ch_status_list = game_info.player1.characters[pos.value].status
            summons = game_info.player1.summon_zone
        else:
            if game_info.player2.dice_zone:
                dice = [str(die) for die in game_info.player2.dice_zone]
            else:
                dice = []
            pos = game_info.player2.active_character_position
            if pos.value is not None:
                ch = game_info.player2.characters[pos.value].character
                ch_status_list = game_info.player2.characters[pos.value].status
            summons = game_info.player2.summon_zone

        action_type = str(type(action)).strip(">'").split(".")[-1]
        print(f"{active_player} {action_type}: {action.dict()}")
        print(f"    Current Dice: {dice}")

        if ch is not None:
            print(
                f"    Current Character: {ch.name}, hp: {ch.health_point}, power: {ch.power}/{ch.max_power}, elem attachment: {ch.elemental_attachment}"
            )
        if len(ch_status_list) >= 1:
            print(f"    Current Character Status:")
            for status in ch_status_list:
                print(f"            {status}")
        if summons:
            print(f"    Current Summons:")
            for summon in summons:
                print(f"          {summon['name']}: usages: {summon['usages']}")

        print("\n")
        valid = game.judge_action(action)
        if valid:
            game.step(action)
            game_info = game.encode_game_info()
            if game_info.status == GameStatus.ENDED:
                winner = game_info.winner
                break
        else:
            print(f"The action of {active_player} is invalid. Game End.")
            winner = ~active_player
            break
        if action_cnt >= 100:
            break

    if winner is PlayerID.SPECTATOR:
        print(f"The game is a draw")
    else:
        print(f"The winner is {winner}")
