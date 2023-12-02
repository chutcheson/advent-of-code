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

def minimum_cubes(draws):
    res = {}
    for draw in draws:
        if draw["game_id"] not in res:
            res[draw["game_id"]] = {
                "red" : 0,
                "green" : 0,
                "blue" : 0,
        }
        res[draw["game_id"]]["red"] = max(res[draw["game_id"]]["red"], draw["red"])
        res[draw["game_id"]]["green"] = max(res[draw["game_id"]]["green"], draw["green"])
        res[draw["game_id"]]["blue"] = max(res[draw["game_id"]]["blue"], draw["blue"])
    return res

def game_powers(minimum_game_cubes):
    res = {}
    for game_id, cubes in minimum_game_cubes.items():
        res[game_id] = cubes["red"] * cubes["green"] * cubes["blue"]
    return res

if __name__ == "__main__":
    draws = read_file("input.txt")
    minimum_cubes = minimum_cubes(draws)
    game_powers = game_powers(minimum_cubes)
    print(sum(game_powers.values()))
