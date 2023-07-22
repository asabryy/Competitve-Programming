def orderSum(operands):
    operands.sort()
    return '+'.join(operands)
            

def main():
    additionIn = input()
    operands = additionIn.split("+")

    print(orderSum(operands))
    

if __name__ == "__main__":
    main()