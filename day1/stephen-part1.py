
def main():
    with open("input_stephen") as f:
        raw = f.read().splitlines()

    team1, team2 = zip(*[(int(a), int(b)) for a, b in (line.split() for line in raw)])

    distances = [abs(location1 - location2) for location1, location2 in zip(sorted(team1), sorted(team2))]

    print(sum(distances))

if __name__ == "__main__":
    main()