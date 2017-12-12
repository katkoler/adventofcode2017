#!/usr/bin/env python3

# l=[0,2,7,0]

for l in open('input_day6.txt').readlines():
	l=l.rstrip().split('\t')

l = [int(x) for x in l]
dist = [tuple(l)]

while len(dist) == len(set(dist)):
	max_value = max(l)
	max_index = l.index(max_value) #index of first max_value in list
	if max_value % (len(l)-1) == 0:
		add = max_value // (len(l)-1)
		for i in range(len(l)):
			if max_index != i:
				l[i] += add
				l[max_index] = 0
	elif max_value % (len(l)-1) == 1:
		add = max_value // (len(l)-1)
		for i in range(len(l)):
			if max_index != i:
				l[i] += add
			else:
				l[max_index] = 1
	elif max_value % len(l) == 0:
		add = max_value // len(l)
		l[max_index] = 0
		for i in range(len(l)):
			l[i] += add
	elif max_value // (len(l)-1) == 0:
		add = 1
		for i in range(max_index+1, max_index+1+max_value):
			if i < len(l):
				l[i] += add
			else:
				i = i - len(l)
				if max_index != i:
					l[i] += add
		l[max_index] = 0			
	else: 
		print("another case")						
	dist.append(tuple(l))			

print(dist[-1], len(set((dist))))
