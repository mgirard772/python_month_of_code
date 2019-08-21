def collatz_full(input: list):
    result_list = []
    longest_chain_length = 0
    longest_chain_term = 0
    for term in input:
        current_term = term
        term_list = [term]
        while(current_term != 1):
            #Term is odd
            if(current_term % 2 == 1):
                current_term = 3*current_term + 1
            #Term is even
            else:
                current_term = current_term/2
            term_list.append(int(current_term))
        result_list.append([term, term_list.__len__(), term_list])
        if(term_list.__len__() > longest_chain_length):
            longest_chain_length = term_list.__len__()
            longest_chain_term = term
    return([[longest_chain_term, longest_chain_length], result_list])

def collatz_lighter(input: list):
    longest_chain_length = 0
    longest_chain_term = 0
    for term in input:
        current_term = term
        chain_length = 1
        while(current_term != 1):
            #Term is odd
            if(current_term % 2 == 1):
                current_term = 3*current_term + 1
            #Term is even
            else:
                current_term = current_term/2
            chain_length+=1
        if(chain_length > longest_chain_length):
            longest_chain_length = chain_length
            longest_chain_term = term
    return([[longest_chain_term, longest_chain_length]])

def collatz_even_lighter(start, end):
    longest_chain_length = 0
    longest_chain_term = 0
    term = start
    while(term < end):
        current_term = term
        chain_length = 1
        while(current_term != 1):
            #Term is odd
            if(current_term % 2 == 1):
                current_term = 3*current_term + 1
            #Term is even
            else:
                current_term = current_term/2
            chain_length+=1
        if(chain_length > longest_chain_length):
            longest_chain_length = chain_length
            longest_chain_term = term
        term+=1
    return ([[longest_chain_term, longest_chain_length]])

if __name__ == "__main__":
    result = collatz_even_lighter(2, 1000000)
    print("Longest chain initial term: %d" % result[0][0])
    print("Longest chain length: %d" % result[0][1])