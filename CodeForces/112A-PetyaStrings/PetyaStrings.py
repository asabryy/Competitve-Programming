def compareStrings(first, second):
    firstLower = first.lower()
    secondLower = second.lower()
    if firstLower == secondLower:
        return 0
    elif firstLower < secondLower:
        return -1
    else:
        return 1
            

def main():
    firstString = input()
    secondString = input()
    
    print(compareStrings(firstString, secondString))

if __name__ == "__main__":
    main()