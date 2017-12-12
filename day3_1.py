#!/usr/bin/env python3

p = 277678

r = 1
i = 0
width = 3
dist = 0
loc = [0, 0]

while (r < p):
	i+=1
	r += i*8
	if i > 1:
		width += 2
	if r == p:
		loc = [-i, -i]
		print("bottom right corner")
	for j in range(1,5):
		if (r+(j*(width+1))) == p:	
			loc = [i+1, i+1]
			print(j,"corner from bottom right anti-clockwise")
		if (r+(j*(width+1)+(1/2*(width+1)))) == p:
			loc = [0, i+1]
			print(j, "mid of side from bottom right corner")

	if r < p:
		extra = p-r
		if extra < width+1:
			loc = [i+1, -i+(extra-1)]
			print("on the right side")	
			if extra == 1:
				loc = [i+1, -i]
				print("one over bottom right corner")	
		if width < extra and extra < 2*width:
			extra = extra-(width+1)
			loc = [i+1-extra, -i+width]
			print("on the top side")

		if 2*width < extra and extra < 3*width:
			extra = extra-2*(width+1)
			loc = [i+1-(width+1), -i+width-extra]
			print("on the left side")

		if 3*(width+1) <extra and extra < 4*(width+1):
			extra = extra-3*(width+1)
			loc = [i-width+extra, -i-1]
			print("on the bottom side")

		dist = abs(loc[0]) + abs(loc[1])		

print(p, loc, dist)

