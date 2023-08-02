def whoWon(games):
    gamesList = list(games)
    if gamesList.count('A')  == gamesList.count('D'):
        return "Friendship"
    elif gamesList.count('A') > gamesList.count('D'):
        return "Anton"
    else:
        return "Danik"
            

def main():
    numGames = input()
    games = input()
    print(whoWon(games))


if __name__ == "__main__":
    main()