#Let's first initialize all the data:
Company_Name = ""
Department_of_Employee = ""
Employee_codenumber = ""
Employee_Name = ""
Salary_date_cutoff = 0
Rate_per_hour = 0
Number_of_hours_per_payday = 0
Number_of_hours_overtime = 0
The_number_of_absences_hours = 0
Number_of_hours_of_honorarium = 0
Number_of_hours_in_tardiness = 0
Withholding_tax = 0
SSS_Contribution = 0
Philhealth_Contribution = 0
PagIbig = 100

#And then we need to input all the needed data:
Company_Name = str(input("Enter your Company Name:"))
Department_of_Employee = str(input("Enter your Department:"))
Employee_codenumber = str(input("Enter your Code/Number:"))
Employee_Name = str(input("Enter your name:"))
Salary_date_cutoff = int(input("Enter your salary date cut-off:"))
Rate_per_hour = float(print("Enter the rate per hour:"))
Number_of_hours_per_payday = int(print("Enter the number of hours per payday:"))
Number_of_hours_overtime = int(print("Enter the number of hours overtime:"))
The_number_of_absences_hours = int(print("Enter the number of absences (in hour):"))
Number_of_hours_of_honorarium = int(print("Enter the number of hours of honorarium"))
Number_of_hours_in_tardiness = int(print("Enter the number of tardiness (in hours):"))
Withholding_tax = float(print("Enter the value of the withholding tax:"))
SSS_Contribution = float(print("Enter the value of SSS contribution:"))
HDMF_Contribution = float(print("Enter the value of HDMF Contribution"))
Philhealth_Contribution = float(print("Enter the value of Philhealth COntribution:"))

#We cam mow compute and process the needed data
Basic_pay = Rate_per_hour*Number_of_hours_per_payday
Overtime_pay = Rate_per_hour*Number_of_hours_overtime
Absences = Rate_per_hour*The_number_of_absences_hours
Honorarium = Rate_per_hour*Number_of_hours_of_honorarium