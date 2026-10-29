
# Sports Tournament Ranking System

n = int(input("Enter number of teams: "))
teams = []

for i in range(n):
    team = input("Enter team name: ")
    teams.append(team)

m = int(input("Enter number of matches: "))
matches = []

for i in range(m):
    print("\nMatch", i + 1)

    team1 = input("Enter first team: ")
    score1 = int(input("Enter first team score: "))
    team2 = input("Enter second team: ")
    score2 = int(input("Enter second team score: "))

    matches.append((team1, score1, team2, score2))

# Statistics: [points, goals_for, goals_against]
stats = [[0, 0, 0] for team in teams]

# Process match results
for match in matches:
    team1, score1, team2, score2 = match

    index1 = teams.index(team1)
    index2 = teams.index(team2)

    stats[index1][1] += score1
    stats[index1][2] += score2
    stats[index2][1] += score2
    stats[index2][2] += score1

    # Award points
    if score1 > score2:
        stats[index1][0] += 3
    elif score2 > score1:
        stats[index2][0] += 3
    else:
        stats[index1][0] += 1
        stats[index2][0] += 1

# Sort by points, goal difference, and goals scored
for i in range(n):
    for j in range(n - i - 1):
        gd1 = stats[j][1] - stats[j][2]
        gd2 = stats[j + 1][1] - stats[j + 1][2]

        if (stats[j][0] < stats[j + 1][0] or
            (stats[j][0] == stats[j + 1][0] and gd1 < gd2) or
            (stats[j][0] == stats[j + 1][0] and
             gd1 == gd2 and
             stats[j][1] < stats[j + 1][1])):

            teams[j], teams[j + 1] = teams[j + 1], teams[j]
            stats[j], stats[j + 1] = stats[j + 1], stats[j]

# Display rankings
print("\nSPORTS TOURNAMENT RANKINGS")
print("-" * 65)
print("Rank Team       Played Points GF GA GD")
print("-" * 65)

for i in range(n):
    played = sum(
        1 for match in matches
        if match[0] == teams[i] or match[2] == teams[i]
    )

    points = stats[i][0]
    gf = stats[i][1]
    ga = stats[i][2]
    gd = gf - ga

    print(i + 1, teams[i], played, points, gf, ga, gd)

print("-" * 65)

