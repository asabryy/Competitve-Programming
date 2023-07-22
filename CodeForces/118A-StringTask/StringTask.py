def stringTask(wordIn):
    wordOut = list(wordIn)
    newWord = []
    vowels = ["A","O","Y","E","U","I"]
    for index, letter in enumerate(wordOut):
        if letter.upper() in vowels:
            continue
        else:
            newWord.append(".")
            newWord.append(letter.lower())
        
    return "".join(newWord)
            

def main():
    wordIn = input()    
    print(stringTask(wordIn))
    

if __name__ == "__main__":
    main()