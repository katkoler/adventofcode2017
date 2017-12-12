#!/usr/bin/env python3

all = []

for l in open('input_day5.txt').readlines():
	l=l.rstrip()
	all.append(l)

# all = [0,3,0,1,-3]

all = [int(x) for x in all]

i = 0
t = 0 

while i < len(all):
	k = all[i]
	if all[i] >= 3:
		all[i] -= 1
	else:	
		all[i] += 1
	i += k
	t += 1

print(t)