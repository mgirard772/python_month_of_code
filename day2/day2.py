import string

def solve():
    # Read words, converting to lowercase and stripping punctuation
    with open('input.txt') as f:
        word_list = [word.translate(str.maketrans('', '', string.punctuation)).lower() for line in f for word in line.split()]

    #Gather information using dictionary
    word_dict = {}
    for i in range(len(word_list)):
        if word_list[i] not in word_dict:
            word_dict[word_list[i]] = [word_list[i], 1, len(word_list[i]), i]
        else:
            word_dict[word_list[i]][1] += 1

    #Convert dictionary to list and sort
    word_dict_list = [*word_dict.values()]
    word_dict_list_sorted = sorted(word_dict_list, key=lambda x: (-x[1], -x[2], x[3]))
    col_names = ['Word', 'Frequency', 'Length', 'First Position']

    #Print results
    row_format ="{:>15}" * (len(col_names) + 1)
    print(row_format.format("", *col_names))
    for row in word_dict_list_sorted[0:15]:
        print(row_format.format("", *row))

if __name__ == "__main__":
    solve()