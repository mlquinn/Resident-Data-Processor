"""
		Resident Data Formatter
	This program takes the resulting txt file from Resident Data Collector and
	formats the data into an xml file for future data processing.
@author Michael Quinn
@date September 23, 2018
@version 0.1
"""

print("Formatting file...")
infile = open("ResidentData.txt", "r")
header = infile.readline().split(",")
data = infile.readlines()
infile.close()

outfile = open("residents.xml", "w")
outfile.write("<?xml version='1.0' ?>\n")
outfile.write("<?xml-stylesheet rel='stylesheet' href='resident.css' ?>")
outfile.write("<residents>\n")
outfile.write("\t<header>\n")
outfile.write("\t\t<nameCol>" + header[0] + "</nameCol>\n")
outfile.write("\t\t<ageCol>" + header[1] + "</ageCol>\n")
outfile.write("\t\t<studentCol>" + header[2].rstrip() + "</studentCol>\n")
outfile.write("\t</header>\n")
for line in data:
	tokens = line.split(",")
	outfile.write("\t<resident>\n")
	for i in range(0, len(tokens)):
		if i == 0:
			outfile.write("\t\t<name>")
			outfile.write(tokens[i])
			outfile.write("</name>\n")
		elif i == 1:
			outfile.write("\t\t<age>")
			outfile.write(tokens[i])
			outfile.write("</age>\n")
		elif i == 2:
			outfile.write("\t\t<student>")
			outfile.write(tokens[i].rstrip())
			outfile.write("</student>\n")
	outfile.write("\t</resident>\n")
outfile.write("</residents>")
print("Done!")
