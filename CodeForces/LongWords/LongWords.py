def shortify(word):

    length = len(word)

    if length < 10:
        print(word)
    else:
        first = word[0]
        last = word[-1]
        between = length - 2
        print(first+str(between)+last)

def main():
    size = input()
    for x in range(int(size)):
        inputWord = input()
        shortify(inputWord)


if __name__ == "__main__":
    main()