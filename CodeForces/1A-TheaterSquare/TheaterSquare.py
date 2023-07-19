import math

def main():
    inputValue = list(map(int, input().split(" ") ))

    n = inputValue[0]
    m = inputValue[1]
    a = inputValue[2]

    print(math.ceil(n / a) * math.ceil(m / a))

if __name__ == "__main__":
    main()