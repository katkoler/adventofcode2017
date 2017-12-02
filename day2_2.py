#!/usr/bin/env python3

result = 0

for line in open("./input_day2.txt").readlines():
	line = line.split('\t')
	line[-1]=line[-1].rstrip()
	line = [int(x) for x in line]

	for i in range(len(line)):
		for j in range(len(line)):
			if line[j] % line[i] == 0:
				if line[j] != line[i]:
					result = result + (line[j]/line[i])

print(result)
