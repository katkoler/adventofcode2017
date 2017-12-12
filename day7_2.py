#!/usr/bin/env python3

supporters = []
endnodes = []
subnodes = []
nodes = []

for line in open('input_day7.txt').readlines():
	if "->" in line:
		line = line.rstrip()
		supporters.append(line)
	else:
		line = line.split(" ")
		line = line[0:2]
		line[1] = int(line[1].strip().strip("(").strip(")"))
		endnodes.append(line)


for i in range(len(supporters)):
	node = supporters[i].strip().split("->")
	node[1] = node[1].strip().split(", ")
	node[0] = node[0].strip().split(" ")
	node[0][1] = int(node[0][1].strip("(").strip(")"))
	node[0].append(node[1])
	nodes.append(node[0])

	# for k in range(len(node)):
	# 	subnode[k] = subnode[k].strip()
	# 	subnodes.append(subnode[k])
print(nodes)

# firstnode = "ahnofa"
firstnode = "tknk"

m = 5
new_nodes = []
for i in range(m):
	for i in range(len(nodes)):
		for j in range(len(nodes[i][2])):
			for k in range(len(endnodes)):
				if nodes[i][2][j] == endnodes[k][0]:
					nodes[i][2][j] = int(endnodes[k][1])

	print("+++++++++++++")

	endnodes = []

	for i in range(len(nodes)):
		if len(set(nodes[i][2])) == 1:
			nodes[i][1] = nodes[i][1] + len(nodes[i][2])*nodes[i][2][0]
			del(nodes[i][2])
		if len(nodes[i]) == 2:
			endnodes.append(nodes[i])
		elif len(nodes[i]) == 3:
			new_nodes.append(nodes[i])
			#add condition that if all numbers but dont match. find the member. and find what is the difference. find what the weight should be		
	nodes = new_nodes
	new_nodes = []
	print("nodes", nodes) 
	print("endnodes", endnodes)



