def takeStones(size, stones):
    stonesSplit = list(stones)
    found = []
    count = 0
    for x in range(size):
        if x == 0:
            found.append(stonesSplit[x])
        elif stonesSplit[x] == stonesSplit[x-1]:
            count += 1
        else:
            found.append(stonesSplit[x])

    return count
            

def main():
    size = input()
    stones = input()    
    print(takeStones(int(size), stones))
    

if __name__ == "__main__":
    main()