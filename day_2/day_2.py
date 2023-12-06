
red_lim = 12
green_lim = 13
blue_lim = 14
limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}
def check_game(game_input):
    games = game_input.split("; ")
    for game in games:
        for color in game.split(", "):
            lim = limits.get(color.split(" ")[1])
            if int(color.split(" ")[0]) > lim:
                return False
    return True


def get_valid_games(game_input):
    game_input_list = [y for y in (x.strip() for x in game_input.splitlines()) if y]
    result = []
    for game in game_input_list:
        game_data = game.split(": ")
        if check_game(game_data[1]):
            result.append(game_data[0])

    return result


def get_sum_of_valid_games(game_input):
    list_of_valid_games = get_valid_games(game_input)
    result_sum = 0
    for val_game in list_of_valid_games:
        result_sum += int(val_game.split(" ")[1])
    return result_sum

##### PART 1 #####


with open('game_input.txt', 'r') as file:
    game_input = file.read()
print(get_sum_of_valid_games(game_input))
