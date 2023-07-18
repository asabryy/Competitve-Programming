def main():
    size = input()
    total = [0,0,0]
    numSol = 0
    for x in range(int(size)):
        sum = 0
        userSol = input()
        for i in userSol.split(" "):
            sum += int(i)
        
        if sum > 1:
            numSol += 1
    
    print(numSol)

if __name__ == "__main__":
    main()