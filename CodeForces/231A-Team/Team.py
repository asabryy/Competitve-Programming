def main():
    size = input()
    total = [0,0,0]
    numSol = 0
    for x in range(int(size)):
        cando = 0
        userSol = input()
        userInt = list(map(int, userSol.split(" ") ))
        cando = sum(userInt)
        
        if cando> 1:
            numSol += 1
    
    print(numSol)

if __name__ == "__main__":
    main()