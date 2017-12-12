#!/usr/bin/env python3

password = 0

def compare(s, t):
    return sorted(s) == sorted(t)

for line in open('input_day4.txt').readlines():
    f = line.split(" ")
    f[-1]=f[-1].rstrip()
    true_list = []
    if len(f) == len(set(f)):
        for j in range(len(f)):
            for i in range(len(f)):
                if j != i: 
                    true_list.append(compare(list(f[i]), list(f[j])))
    
    if len(set(true_list)) == 1:
        password += 1

print(password)
