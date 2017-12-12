#!/usr/bin/env python3

supporters = []
subnodes = []
nodes = []

for line in open('input_day7.txt').readlines():
	if "->" in line:
		line = line.rstrip()
		supporters.append(line)

for i in range(len(supporters)):
	node = supporters[i].split("->")
	subnode = node[1]
	node = node[0].strip().split(" ")
	subnode = subnode.split(",")
	nodes.append(node[0])
	for k in range(len(subnode)):
		subnode[k] = subnode[k].strip()
		subnodes.append(subnode[k])

for i in range(len(nodes)):
	if nodes[i] not in subnodes:
		print(nodes[i])
