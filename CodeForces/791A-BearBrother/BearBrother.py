def bearYears(weights):
    a = int(weights[0])
    b = int(weights[1])
    count = 0
    while True:
        if a > b:
            break
        else:
            a = 3*a
            b = 2*b
            count += 1
    
    return count
            

def main():
    weights = input().split(" ")
    print(bearYears(weights))

    

if __name__ == "__main__":
    main()