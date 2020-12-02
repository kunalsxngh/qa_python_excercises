f = open("teams.txt", "x")
f.close()
teams = ["MANUTD", "ARS", "CHEL", "MANCITY", "SPURS"]

with open("teams.txt", "w") as f:
    for n in teams:
        newline = n + "\n"
        f.write(newline)

f = open("teams.txt", "r")
outfile = ""

for line in range(1,5):
    if line == 1 or line ==4:
        outfile += f.readline()
    else:
        f.readline()

print(outfile)