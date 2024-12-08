
def main():
    with open("input") as f:
        raw = f.read().splitlines()
        team1mol = []
        team2mol = []
        for each in raw:
            r1, r2 = each.split("   ")
            team1mol.append(int(r1))
            team2mol.append(int(r2))

    print(team1mol)
    print(team2mol)


if __name__ == "__main__":
    main()