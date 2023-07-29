def isIdeal(forces):
    x = 0
    y = 0
    z = 0

    for vec in forces:
        vector = list(map(int, vec.split(" ")))
        x += vector[0]
        y += vector[1]
        z += vector[2]

    if (x == 0) and (y == 0) and (z == 0):
        return "YES"
    else:
        return "NO"

def main():
    size = int(input())
    forces =[]
    for x in range(size):
        forces.append(input())
    print(isIdeal(forces))
    

if __name__ == "__main__":
    main()