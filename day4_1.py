#!/usr/bin/env python3

i = 0

for line in open('input_day4.txt').readlines():
    f = line.split(" ")
    f[-1]=f[-1].rstrip()
    if len(f) == len(set(f)):
        i += 1

print(i)