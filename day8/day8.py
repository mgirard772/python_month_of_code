
def solve():
    input = [0,1,0,2,1,0,1,3,2,1,2,1]
    height_difference_last = []
    height_difference_max = []
    max_height = 0
    total_rainwater = 0
    for i in range(len(input)):
        total_rainwater += max(0,max_height-input[i])
        max_height = max(max_height,input[i])
        if i == 0:
            height_difference_last.append(0)
            height_difference_max.append(0)
        else:
            height_difference_last.append(input[i] - input[i-1])
            height_difference_max.append(input[i] - max_height)

    print(total_rainwater)

if __name__ == "__main__":
    solve()