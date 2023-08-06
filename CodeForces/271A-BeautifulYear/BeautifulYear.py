def nextDistinct(year):
    tempYear = int(year)
    while True:
        tempYear += 1
        strYear = set(list(str(tempYear)))
        if len(strYear) == 4:
            return tempYear
            

def main():
    year = input()
    print(nextDistinct(year))
    

if __name__ == "__main__":
    main()