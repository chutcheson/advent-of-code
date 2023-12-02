def read_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        game_id = int(line.split(":")[0][5:])
        draws = [draw.strip() for draw in line.split(":")[1].strip().split(";")]
        for draw in draws:
            game_draw = {
                "game_id": game_id,
                "red" : 0,
                "green" : 0,
                "blue" : 0,
            }
            cubes = [cube.strip() for cube in draw.split(",")]
            for cube in cubes:
                count, color = cube.split(" ")
                game_draw[color] = int(count)
            data.append(game_draw)
    return data

def check_games(draws):
    all_games = set()
    impossible_games = set()
    for draw in draws:
        all_games.add(draw["game_id"])
        if draw["red"] > 12 or draw["green"] > 13 or draw["blue"] > 14:
            impossible_games.add(draw["game_id"])
    return all_games - impossible_games

if __name__ == "__main__":
    print(sum(check_games(read_file("input.txt"))))




