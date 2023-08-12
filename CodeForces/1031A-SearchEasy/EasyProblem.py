def isEasy(people):
    peopleListSet = set(people.split(" "))
    if "1" in peopleListSet:
        return "HARD"
    return "EASY"

def main():
    size = int(input())
    people = input()
    print(isEasy(people))
    

if __name__ == "__main__":
    main()