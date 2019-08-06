def unique_paths(m:int = 2, n:int = 2):
    # If either given row number is first
    # or given column number is first
    if(m <= 0 or n <= 0):
        raise ValueError("Improper arguments given, m or n <= 0!")
    if (m == 1 or n == 1):
        return 1
    else:
        return unique_paths(m - 1, n) + unique_paths(m, n - 1)

def unique_paths_2(x:int = 1, y:int = 1, x_size:int = 2, y_size:int = 2, current_path:str = '(1,1)'):
    path_list = []
    if(x == x_size and y == y_size):
        path_list.append(current_path)
    else:
        if(x == x_size):
            path_list = path_list + unique_paths_2(x, y+1, x_size, y_size, current_path + ' -> (%d,%d)' % (x, y+1))
        elif(y == y_size):
            path_list = path_list + unique_paths_2(x+1, y, x_size, y_size, current_path + ' -> (%d,%d)' % (x+1, y))
        else:
            path_list = path_list + unique_paths_2(x, y+1, x_size, y_size, current_path + ' -> (%d,%d)' % (x, y+1))
            path_list = path_list + unique_paths_2(x+1, y, x_size, y_size, current_path + ' -> (%d,%d)' % (x+1, y))
    return path_list

if __name__ == "__main__":
    print('Solution 1 paths count: %d' % unique_paths(10,5))
    path_list = unique_paths_2(x_size=10, y_size=5)
    print('Solution 2 paths count: %d' % len(path_list))
    print('Solution 2 path list: ')
    for path in path_list:
        print(path)
