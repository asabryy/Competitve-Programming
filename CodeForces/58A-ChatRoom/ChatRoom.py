def isHello(word):
    hello = list("hello")
    index = 0
    for letter in word:
        if letter == hello[index]:
            index += 1
        if index == 5:
            return "YES"
    
    return "NO"
    

            

def main():
    word = input()
    print(isHello(word))
    

if __name__ == "__main__":
    main()