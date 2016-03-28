import csv
import sys
import os

print("FFXIV Achievement Database Generator")
print("Written by Catuse167 of FFWiki - Ver. 1.0")

file = raw_input("What is the name of the CSV file? ")

"""with open('LuaData/meta.lua','ab') as f:
	patch = raw_input("What patch of FFXIV is this? ")
	print("Reporting metadata to LuaData/meta.lua...")
	f.write("\tachvPatch = " + patch + ",\n")

items = []
titles = []
icons = ""

with open(raw_input('What is the name of the items CSV? '),'rb') as itemfile:
	print("Reading from items CSV.")
	reader = csv.DictReader(itemfile)
	for row in reader:
		items.append(row['name'])
		
with open(raw_input('What is the name of the titles CSV? '),'rb') as titlesfile:
	print("Reading from titles CSV.")
	reader = csv.DictReader(titlesfile)
	for row in reader:
		titles.append(row['Name'])"""
	
with open(file, 'rb') as csvfile:
	print("Reading from " + file + ".")
	reader = csv.DictReader(csvfile)
	typeset = []
	for i in xrange(0,94):
		typeset.append("")
	print("Printing achievement data to LuaData/achievements.lua.")
	for row in reader:
		if row['Name']:
			typeset[int(row['Category'])] += row['Name'] + "; "
			
			"""icon = row['Icon']
			src = ""
			if int(icon) < 10:
				src = "ui/icon/00000" + icon + ".tex.png"
			elif int(icon) < 100:
				src = "ui/icon/0000" + icon + ".tex.png"
			elif int(icon) < 1000:
				src = "ui/icon/000" + icon + ".tex.png"
			elif int(icon) < 10000:
				src = "ui/icon/00" + icon + ".tex.png"
			elif int(icon) < 100000:
				src = "ui/icon/0" + icon + ".tex.png"
			elif int(icon) < 1000000:
				src = "ui/icon/" + icon + ".tex.png"
			else:
				print("No icon for " + row['Name'] + "!")
				with open('logs/error.log','ab') as errlog:
					errlog.write("No icon for " + row['Name'] + "!")
			if src:
				try:
					os.rename(src, "filesToUpload/FFXIV " + row['Name'] + " Icon.png")
					icons += "[" + icon + "]=\""File:FFXIV " + row['Name'] + " Icon.png"\","
				except WindowsError:
					with open('error.log','ab') as errlog:
						errlog.write("No icon for " + row['Name'] + "!")
			
			
			if row['Title'] and row['Title'] != "0":
				reward = "Title: " + titles[int(row['Title'])]
			elif row['Item'] and row['Item'] != "0":
				reward = "Item: " + items[int(row['Item'])]
			else:
				reward = ""
			
			written = "[\"" + row['Name'] + "\"]={"
			written += "id=" + row['Index'] + ","
			written += "typ=" + row['Category'] + ","
			written += "ico=" + icon + ","
			written += "desc=\"" + row['Description'] + "\","
			if reward:
				written += "rwd=\"" + reward + "\","
			written += "pts=" + row['Points'] + ","
			written += "},\n"
			with open('LuaData/achievements.lua','ab') as f: f.write(written)"""
				
print("Printing achievement sets sets to Wikitext/achvsets.py.")
with open('Wikitext/achvsets.py','ab') as f: f.write(str(typeset))
"""print("Printing icon list to sets to LuaData/icons.lua")
with open('LuaData/icons.lua','ab') as f: f.write(icons)"""