import copy
def solve(v: list):
    #Initialize stack
    stack = []
    #Create stack from list
    while (v.__len__() > 0):
        stack.append(v.pop())
    #Find next greatest for each element
    while(stack.__len__() > 0):
        num = stack.pop()
        next_greater = 'Inf'
        greater_stack = copy.deepcopy(stack)
        while(greater_stack.__len__() > 0):
            next = greater_stack.pop()
            if(next > num):
                next_greater = next
                break
        print("%d & %s" % (num, next_greater))


if __name__ == "__main__":
    v = [1, 5, 18, 7, 19, 12, 10, 1]
    solve(v)