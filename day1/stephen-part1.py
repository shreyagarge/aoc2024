
def main():
    with open("input") as f:
        raw = f.read().splitlines()

    team1bun, team2bun = zip(*(i.split() for i in raw))
    print(team1bun)
    print(team2bun)


if __name__ == "__main__":
    main()