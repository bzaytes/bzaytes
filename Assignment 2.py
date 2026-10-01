# Program Name: Assignment2.py (use the name the program is saved as)
# Course: IT3883/Section W01(85546)
# Student Name: Tesfaye Woldemariam
# Assignment Number: Assignment 2 
# Due Date: 10/02/ 2026
# Purpose: What does the program do (in a few sentences)? The python code Initializes an empty input buffers and offer a menue user to append data ,clear the buffer ,display its contents or exit the program 


def calculate_final_averages(input_file):
    students = []

    #Read input file
    with open(input_file, 'r')as file:
        for line in file:
            #parse the line
            parts = line.split()

            # The first part is the name ,therest are scorees
            name = parts[0]
            scores = list(map(float, parts[1:]))

            #calculate the average of the scores
            final_average = sum(scores) / len(scores)

            #Store name and average 
            students.append((name, final_average))

    #Sort the students by final average in decending order
    students.sort(key=lambda x: x[1],reverse=True)

    #Display results
    for student in students:
        print(f"{student[0]} {student[1]:.2f}")

calculate_final_averages('input.txt')
