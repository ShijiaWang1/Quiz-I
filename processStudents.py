''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv
from xml.etree.ElementPath import get_parent_map


# create a file object to open the file in read mode

student = open("students.csv", "r")


# create a csv object from the file object
student_file = csv.reader(student, delimiter=",")


#skip the header row
next(student_file)

#create an outfile object for the pocessed record

sutdent_outfile = csv.writer(open("processedStudents.csv", "a", newline=""), delimiter=",")

#create a new dictionary named 'student_dict'

student_dict = {"student_id": {"gpa"}
}

#use a loop to iterate through each row of the file
for record in student_file:
    #check if the GPA is below 3.0. If so, write the record to the outfile
    gpa=float(record[8])
    if gpa < 3:
        sutdent_outfile.writerow((record[0], record[2], record[3],record[6],record[7],record[8]))
        student_dict['student id'] =(record[0])
        student_dict["gpa"] =(record[8])

    
    # append the record to the dictionary with the student id as the Key
    # and the value as the GPA


#print the entire dictionary
print(student_dict)

#Print the student id 
print(student_dict['student id'])

#print out the corresponding GPA from the dictionary

print(student_dict["gpa"])

#close the outfile

student.close






