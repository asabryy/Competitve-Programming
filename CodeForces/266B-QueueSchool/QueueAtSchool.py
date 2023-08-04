def moveQueue(size, time, queue):
    queueList = list(queue)
    for x in range(int(time)):
        i = 0
        while (i<int(size)):
            if i == 0:
                i+=1
                continue
            elif (queueList[i] == 'G') and (queueList[i-1] == 'B'):
                queueList[i], queueList[i-1] = queueList[i-1], queueList[i]
                i+=1
            i+=1

    
    return "".join(queueList)
            

def main():
    size, time = input().split(" ")
    queue = input()    
    print(moveQueue(size, time, queue))
    

if __name__ == "__main__":
    main()