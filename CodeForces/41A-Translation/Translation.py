def isTranslated(first, second):
    if first == second[::-1]:
        return "YES"
    else:
        return "NO"
            

def main():
    firstString = input()
    secondString = input()
    
    print(isTranslated(firstString, secondString))

if __name__ == "__main__":
    main()