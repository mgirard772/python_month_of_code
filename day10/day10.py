def is_valid(input: list):
    square_counts = [{} for i in range(0,9)]
    horizonal_counts = [{} for i in range(0,9)]
    for x in range(len(input)):
        counts = {}
        for y in range(len(input[i])):

            counts[i] = counts.get(i, 0) + 1
        count_list.append(counts)
    return(count_list)

def build_lookups():
    square_lookup = []
    for x in range(0,9):
        if x < 3:
            square_lookup.append([y for y in range(0,3) for x in range(0,3)])
        elif x < 6:
            square_lookup.append([y for y in range(3,6) for x in range(0,3)])
        else:
            square_lookup.append([y for y in range(6,9) for x in range(0,3)])
    return(square_lookup)




if __name__ == "__main__":
    valid_input = \
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
    invalid_input = \
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]