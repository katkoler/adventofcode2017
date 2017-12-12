#!/usr/bin/env python3

result = 0

for line in open("./input_day2.txt").readlines():
	line = line.split('\t')
	line[-1]=line[-1].rstrip()
	line = [int(x) for x in line]
	mins = min(line)
	maxs = max(line)
	result = result + (maxs-mins)

print(result)
