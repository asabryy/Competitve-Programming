def boyOrGirl(wordIn):
    if len(set(wordIn))%2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"
            

def main():
    wordIn = input()
    print(boyOrGirl(wordIn))
    

if __name__ == "__main__":
    main()