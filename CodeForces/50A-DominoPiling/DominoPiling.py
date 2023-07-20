def getDominos(m, n):
    return int((m*n)/2)

            

def main():
    firstLine = input().split(" ")
    m = int(firstLine[0])
    n = int(firstLine[1])

    print(getDominos(m, n))
    

if __name__ == "__main__":
    main()