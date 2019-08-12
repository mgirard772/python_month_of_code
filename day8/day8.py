
def solve(input):
    max_height = 0
    rain_water_tracker = []
    for i in range(len(input)):
        if input[i] < max_height:
            new_max = max(input[i:])
            if new_max >= max_height:
                rain_water_tracker.append(max_height - input[i])
            else:
                rain_water_tracker.append(new_max - input[i])
        else:
            max_height = max(max_height, input[i])
            rain_water_tracker.append(0)
    return rain_water_tracker

if __name__ == "__main__":
    input = [0, 3, 1, 2, 0, 0, 3, 1, 4, 1, 3, 2, 1, 0, 1, 0]
    rain_water_tracker = solve(input)
    print("Rain Water Results")
    print(rain_water_tracker)
    print("Total Units of Rain Collected: ", sum(rain_water_tracker))