#Initialize the net income, the gross income, the total deduction, the name of the employee, and
#Pag-ibig Contribution
net_income = 0
gross_income = 0
total_deduction = 0
name_of_the_employee = ""
pagibig_contribution = 100

#Then input the name of the employee, the rate per hour, number of hours per day, number of days per week, number of weeks per month, sss
#contribution, philhealth contribution, tax contribution
name_of_the_employee = str(input("Enter Employee's Name:"))
rate_per_hour = float(input("Enter Employee's rate per hour:"))
number_of_hours_per_day = float(input("Enter Employee's number of working hours per day:"))
number_of_days_per_week = int(input("Enter Employee's number of working days per week:"))
number_of_week_per_month = int(input("Enter Employee's number of working week per month:"))
sss_contribution = float(input("Enter Employee's SSS Contribution:"))
philhealth_contribution = float(input("Enter Employee's PhilHealth Contribution:"))
tax_contribution = float(input("Enter Employee's Tax Contribution:"))

#Compute the gross income, total deduction
gross_income = rate_per_hour*number_of_hours_per_day*number_of_days_per_week*number_of_week_per_month
total_deduction = sss_contribution+philhealth_contribution+tax_contribution+pagibig_contribution
net_income = gross_income-total_deduction

#Display the name of the name of the employee, the rate per hour, number of hours per day, number of days per week, number of weeks per month, sss
#contribution, philhealth contribution, tax contribution
print("Name of the Employee: ", name_of_the_employee)
print("Net Income: ", net_income)
print("Gross Income: ", gross_income)
print("Total Deduction: ", total_deduction)