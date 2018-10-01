"""
		Resident Data Collector!
	A simple Program for collecting data to be saved onto a file for future
	processing.
@author Michael Quinn
@date September 23, 2018
@version 0.1
"""

print("\tResident Data Collector!")
outfile = open("ResidentData.txt","w")
outfile.write("name, age, student\n")
done = False
while (not done) :
	resident = input("enter your name , age, and student status seperated" +
	" by a comma. Enter 'done' when finished: ").strip().lower()
	if resident == 'done' :
		done = True
	else :
		outfile.write(resident.replace(" " ,"") + "\n")
outfile.close()
print("Thanks for the data!")