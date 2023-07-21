def movesToCenter(row, col):
    rowMoves = abs(2 - row)
    colMoves = abs(2 - col)

    totalMoves = rowMoves + colMoves

    return totalMoves
            

def main():
    row = 0
    col = 0
    line = "" 

    while True:
        temp = input()
        if "1" in temp:
            line = temp.split(" ")
            col = line.index("1")
            break
        else:
            row += 1
    
    print(movesToCenter(row, col))
    

if __name__ == "__main__":
    main()