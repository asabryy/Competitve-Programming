def steps(distance):
    diff = distance%5
    total = distance/5
    
    if diff > 0:
        diff = 1
    else:
        diff = 0

    return int(total) + diff
    
            

def main():
    distance = int(input())
    print(steps(distance))
    

if __name__ == "__main__":
    main()