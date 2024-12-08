import collections


def main():
    with open("input_shreya") as f:
        raw = f.read().splitlines()
        team1 = []
        team2 = []
        for each in raw:
            r1, r2 = each.split()
            team1.append(int(r1))
            team2.append(int(r2))

    diff = difference(team1, team2)
    sim = similarity(team1, team2)

    print(sim)


def difference(team1, team2):
    diff = 0
    for l1, l2 in zip(sorted(team1), sorted(team2)):
        diff += abs(l2 - l1)
    return diff


def similarity(team1, team2):
    sim = 0
    team1hashmap = collections.Counter(team1)
    team2hashmap = collections.Counter(team2)
    for each in team1hashmap:
        sim += team2hashmap[each] * team1hashmap[each] * each

    return sim

if __name__ == "__main__":
    main()