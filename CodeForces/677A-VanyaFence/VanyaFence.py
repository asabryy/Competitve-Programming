def minWidth(numFriends, fenceHeigh, friends):
    count = 0
    friendsList = friends.split(" ")
    for x in friendsList:
        if int(x) > int(fenceHeigh):
            count += 1
    total = len(friendsList) + count

    return total
    
            

def main():
    numFriends, fenceHeight = input().split(" ")
    friends = input()
    print(minWidth(numFriends, fenceHeight, friends))
    

if __name__ == "__main__":
    main()