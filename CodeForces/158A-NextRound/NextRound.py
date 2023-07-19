def getWinners(n, k, scores):
    pos = 0
    kthScore = scores[k-1]

    if kthScore == 0:
        return 0
    else:
        for i in range(k-1, n-1):
            if scores[i] < kthScore:
                pos = i
                break

        if pos == 0:
            return n
        else:
            return pos
            

def main():
    firstLine = input().split(" ")
    n = int(firstLine[0])
    k = int(firstLine[1])
    scores = list(map(int, input().split(" ") ))

    print(getWinners(n, k, scores))
    

if __name__ == "__main__":
    main()