def almostLucky(number):
    luckyNumber = {'7', '4'}
    print(int(number)%4, int(number)%7)
    if set(list(number)) == luckyNumber:
        return "YES"
    elif (int(number)%4 == 0) or (int(number)%7 == 0):
        return "YES"
    return "NO"
            

def main():
    number = input()
    print(almostLucky(number))
    

if __name__ == "__main__":
    main()