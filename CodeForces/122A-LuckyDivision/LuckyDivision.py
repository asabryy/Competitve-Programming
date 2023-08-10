import itertools

def almostLucky(number):
    luckyNumber = [4, 7, 47, 74, 447, 477, 744, 774, 747, 474]
    for x in luckyNumber:
        if int(number)%x == 0:
            return "YES"
    return "NO"
    
            

def main():
    number = input()
    print(almostLucky(number))
    

if __name__ == "__main__":
    main()