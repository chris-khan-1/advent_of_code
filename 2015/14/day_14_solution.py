from collections import defaultdict


def parse_raw_reindeer_info(input: list[str]) -> dict[dict]:
    reindeer_info = defaultdict(dict)
    for info_string in input:
        info_list = info_string.split(" ")
        name = info_list[0]

        reindeer_info[name] = {
            "speed": int(info_list[3]),
            "fly_time": int(info_list[6]),
            "rest_time": int(info_list[-2]),
        }
    return reindeer_info


def get_distance_given_time(reindeer_info: dict[dict], reindeer: str, time: int) -> int:
    elapsed_time = 0
    interval_time = 0
    distance = 0
    info = reindeer_info[reindeer]
    while elapsed_time < time:
        elapsed_time += 1
        interval_time += 1
        distance += info["speed"]  # distance in 1 second
        if interval_time % info["fly_time"] == 0:  # fly_time complete
            elapsed_time += info["rest_time"]  # rest
            interval_time = 0  # reset interval time
    return distance


def get_winning_distance(input: list[str], time: int) -> int:
    reindeer_info = parse_raw_reindeer_info(input=input)
    best_distance = 0
    for reindeer in reindeer_info.keys():
        distance = get_distance_given_time(
            reindeer_info=reindeer_info, reindeer=reindeer, time=time
        )
        if distance > best_distance:
            best_distance = distance
    return best_distance


# very inneficient, calculating the whole distance each time...
def get_winning_points(input: list[str], time: int) -> int:
    reindeer_info = parse_raw_reindeer_info(input=input)
    current_distances = defaultdict(int)
    points = defaultdict(int)
    elapsed_time = 0
    while elapsed_time < time:
        elapsed_time += 1
        for reindeer in reindeer_info.keys():
            current_distances[reindeer] = get_distance_given_time(
                reindeer_info=reindeer_info, reindeer=reindeer, time=elapsed_time
            )
        winner_distance = max(current_distances.values())
        winners = [k for k, v in current_distances.items() if v == winner_distance]
        for winner in winners:
            points[winner] += 1
    return max(points.values())


if __name__ == "__main__":
    with open("./2015/14/input.txt", "r") as input_file:
        input = [line.strip() for line in input_file.readlines()]
        winning_distance = get_winning_distance(input=input, time=2503)
        winning_points = get_winning_points(input=input, time=2503)

    with open("./2015/14/solution.txt", "w") as output_file:
        output_file.write(
            f"Part 1: The distance of the winner is {winning_distance}.\n"
        )
        output_file.write(f"Part 2: The winning number of points is {winning_points}.")
