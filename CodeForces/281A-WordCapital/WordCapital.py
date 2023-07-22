def wordCap(wordIn):
    wordOut = list(wordIn)
    wordOut[0] = wordOut[0].upper()
    return "".join(wordOut)
            

def main():
    wordIn = input()
    print(wordCap(wordIn))
    

if __name__ == "__main__":
    main()