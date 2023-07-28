def howMuch(values):
    k = int(values[0])
    n = int(values[1])
    w = int(values[2])

    kw = k * w

    seqSum = w*((k+kw)/2) #arth equence sum
    
    diff =  int(seqSum - n)

    if diff <= 0:
        return 0
    else:
        return diff
    
            

def main():
    values = input().split(" ")
    print(howMuch(values))
    

if __name__ == "__main__":
    main()