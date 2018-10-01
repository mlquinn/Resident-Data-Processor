"""
		Resident Data Formatter
	This program takes the resulting xml file from Resident Data Formatter and
	processes the data as a whole to determine several things such as the average
	age of all residents, students, and nonstudents.
@author Michael Quinn
@date September 26, 2018
@version 0.2
"""
from bs4 import BeautifulSoup

print("Processing...")
infile = open("residents.xml", "r")
contents = infile.read()
infile.close()
soup = BeautifulSoup(contents, "xml")
residents = soup.find_all("resident")
i = 0
student = 0
studentAge = 0
nonstudent = 0
nonstudentAge = 0
for resident in residents:
	if residents[i].student.getText() == 'yes':
		student += 1
		studentAge += float(residents[i].age.getText())
	elif residents[i].student.getText() == 'no':
		nonstudent += 1
		nonstudentAge += float(residents[i].age.getText())
	i += 1
print("There are a total of " + str(student) + " students.\n" +
 "Average age of student residents: " + str(float(studentAge/student)))
print("There are a total of " + str(nonstudent) + " nonstudents.\n" +
 "Average age of nonstudent residents: " + str(float(nonstudentAge/nonstudent)))