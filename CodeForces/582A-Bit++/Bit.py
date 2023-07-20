def getX(statment):
    if ("++" in statment) and ("X" in statment):
        return 1
    elif ("--" in statment) and ("X" in statment):
        return -1
    
    return None
            

def main():
    numStatments = input()
    x = 0
    for i in range(int(numStatments)):
        statment = input()
        x += getX(statment)
    
    print(x)


if __name__ == "__main__":
    main()