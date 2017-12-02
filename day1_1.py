#!/usr/bin/env python3

result = 0

one = open("./input_day1.txt").read().strip()
one = [int(x) for x in one]
one.append(one[0])
for j in range(len(one)):
	if j+1 < len(one):
		if one[j] == one[j+1]:
			result += (one[j])

print(result)