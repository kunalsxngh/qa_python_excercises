f = open("teams.txt", "x")
f.close()
teams = ["MANUTD", "ARS", "CHEL", "MANCITY", "SPURS"]

with open("teams.txt", "w") as f:
    for n in teams:
        newline = n + "\n"
        f.write(newline)