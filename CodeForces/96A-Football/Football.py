def isDanger(lineup):
    lineup = list(lineup)
    danger = "NO"
    count = 1
    for i in range(len(lineup)):
    
        if i == 0:
            continue
        elif lineup[i] == lineup[i-1]:
            count += 1
        else:
            count = 1

        if count == 7:
            danger = "YES"
            break
            
    return danger


def main():
    lineup = input()
    print(isDanger(lineup))



if __name__ == "__main__":
    main()