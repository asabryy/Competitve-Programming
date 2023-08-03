def minCap(passengerList):
    min = None
    total = 0
    for x in passengerList:
        total = total - int(x[0]) + int(x[1])
        if min == None:
            min = total
        elif total > min:
            min = total
    
    return min

            

def main():
    stops = int(input())
    passengerList = []
    for x in range(stops):
        passengerList.append(input().split(" "))
    
    print(minCap(passengerList))

if __name__ == "__main__":
    main()