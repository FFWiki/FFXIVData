import csv
import sys
import os
"""
file = raw_input("What is the name of the CSV file? ")
ulog = raw_input("What is the name of the upload log? ")"""

file = "item.exh_en3.21.csv"
ulog = "allicons.txt"

list = []
lines = []
output = ""
for i in xrange(0,100000):
	list.append([])

with open(file, 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['name']:
			list[int(row['iconID'])].append(row['name'])

with open(ulog, 'rb') as ulfile:
	for line in ulfile:
		line = line.split("\n")[0]
		lines.append(line)
		
for a in xrange(0,100000):
	if list[a] != []:
		for line in lines:
			for name in list[a]:
				if ("File:FFXIV " + name + " Icon.png") in line:
					output += "[" + str(a) + "]=\"" + line + "\","
					break
					
with open("LuaData/icons.lua", 'ab') as opfile:
	opfile.write(output)