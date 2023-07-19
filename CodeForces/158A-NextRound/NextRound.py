def getWinners(n, k, scores):
    total = 0
    kthScore = scores[k-1]

    for score in scores:
        if (score >= kthScore) and score != 0:
            total += 1 

    return total
            

def main():
    firstLine = input().split(" ")
    n = int(firstLine[0])
    k = int(firstLine[1])
    scores = list(map(int, input().split(" ") ))

    print(getWinners(n, k, scores))
    

if __name__ == "__main__":
    main()