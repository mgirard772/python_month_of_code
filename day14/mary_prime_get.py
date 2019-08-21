import sys
def isP(n: int):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return(False)
        return(True)
    else:
        return(False)
if __name__ == "__main__":
    min, max = int(sys.argv[1]), int(sys.argv[2])
    r = [x for x in range(max, min - 1, -1) if isP(x) and x != 2]
    rs = []
    for n in r:
        if(isP(sum(rs) + n)):
            rs.append(n)
    print(sum(rs[0:3]))