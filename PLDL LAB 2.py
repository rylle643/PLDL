# Initialize the Final Grade
Final_Grade = 0

# Input the Student name, final quizzes, final research/assignment,
# final project, and final exam ratings
student_name = str(input("Enter Student's Name: "))
final_quizzes = float(input("Enter Ratings for Final Quizzes: "))
final_research_assignment = float(input("Enter Ratings for Final Research/assignment: "))
final_project = float(input("Enter Ratings for Final Project: "))
final_exam = float(input("Enter Ratings for Final Exam: "))

# Compute the Final Grade
Final_Grade = (0.30 * final_quizzes) + (0.10 * final_research_assignment) + (0.40 * final_exam) + (0.20 * final_project)

# Determine the final grade's grading remarks
if Final_Grade >= 98:
    Grading_Remarks = 4.00
elif Final_Grade >= 95:
    Grading_Remarks = 3.75
elif Final_Grade >= 92:
    Grading_Remarks = 3.50
elif Final_Grade >= 89:
    Grading_Remarks = 3.25
elif Final_Grade >= 86:
    Grading_Remarks = 3.00
elif Final_Grade >= 83:
    Grading_Remarks = 2.75
elif Final_Grade >= 80:
    Grading_Remarks = 2.50
elif Final_Grade >= 77:
    Grading_Remarks = 2.25
elif Final_Grade >= 74:
    Grading_Remarks = 2.00
elif Final_Grade >= 71:
    Grading_Remarks = 1.75
elif Final_Grade >= 68:
    Grading_Remarks = 1.50
elif Final_Grade >= 64:
    Grading_Remarks = 1.25
elif Final_Grade >= 60:
    Grading_Remarks = 1.00
else:
    Grading_Remarks = 0.00

# Print the student's final grade and grading remarks
print("Student Name: ", student_name)
print("Final Quizzes: ", final_quizzes)
print("Final Research/Assignment: ", final_research_assignment)
print("Final Project: ", final_project)
print("Final Exam: ", final_exam)
print("Final Grade: ", Final_Grade)
print("Grading Remarks: ", Grading_Remarks)

