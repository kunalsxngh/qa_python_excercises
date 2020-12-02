file = open("teams.txt", "r")

outfile = file.readlines()
outfile[0] = "This is a new line\n"

file = open("teams.txt", "w")
file.writelines(outfile)
file.close()