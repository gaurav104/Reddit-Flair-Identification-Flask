
with open("./url.txt") as fp:
	lines = fp.readlines()
	for line in lines:
		print(line.strip())