#!/usr/bin/env python3

result = 0

one = open("./input_day1_1.txt").read().strip()
one = [int(x) for x in one]

for j in range(len(one)//2):
	if j+1 < len(one)/2:
		if one[j] == one[j+len(one)//2]:
			result += 2*one[j]

print(result)