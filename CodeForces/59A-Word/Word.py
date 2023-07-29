def upperLower(word):
    letterList = list(word)
    upper = 0
    lower = 0
    for x in letterList:
        if x.isupper():
            upper += 1
        else:
            lower += 1

    if upper > lower:
        return word.upper()
    else:
        return word.lower()

    
            

def main():
    word = input()
    print(upperLower(word))
    

if __name__ == "__main__":
    main()