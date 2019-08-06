def unique_paths(m, n):
    # If either given row number is first
    # or given column number is first
    if (m == 1 or n == 1):
        return 1
    else:
        return unique_paths(m - 1, n) + unique_paths(m, n - 1)

# col = 5
# row = 10
# expansion = [[x, [y for y in range(col)]] for x in range(row)]

# def unqiue_paths_2(x, y, x_size, y_size):
#     path_list = []
#     if(x == x_size and y == y_size):
#         return "(%d,%d)" % (x,y)
#     else
#         path_list.append()

if __name__ == "__main__":
    print(unique_paths(10,5))