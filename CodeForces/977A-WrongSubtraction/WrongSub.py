def tanyasAlg(number, perm):

    for x in range(perm):
        if number%10 == 0:
            number = number/10
        else:
            number = number-1
    
    return int(number)
            

def main():
    values = input().split(" ")
    number = int(values[0])
    perm = int(values[1])
    print(tanyasAlg(number, perm))

if __name__ == "__main__":
    main()