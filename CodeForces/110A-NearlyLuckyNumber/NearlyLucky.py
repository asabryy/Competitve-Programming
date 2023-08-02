def isLucky(number):
    numberList = list(number)
    notList = ['0', '1', '2', '3', '5' ,'6' ,'8', '9']
    lucky = "YES"
    if ((numberList.count('7') + numberList.count('4')) != 4) and ((numberList.count('7') + numberList.count('4')) != 7):
        lucky = "NO"

    return lucky

            
def main():
    number = input()
    print(isLucky(number))
    

if __name__ == "__main__":
    main()