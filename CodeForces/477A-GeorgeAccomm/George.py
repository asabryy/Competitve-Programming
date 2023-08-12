def canMove(room):
    people, size = room.split(" ")
    if (int(size) - int(people)) > 1:
        return 1
    return 0            

def main():
    count = 0
    numRooms = input()
    for x in range(int(numRooms)):
        room = input()
        count += canMove(room)
    
    print(count)
    

if __name__ == "__main__":
    main()