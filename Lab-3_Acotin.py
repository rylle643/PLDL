#Initialize all the data
#Pag-Ibig Contribution is set as constant
company_name = ""
department_of_employee = ""
employee_codenumber = ""
employee_name = ""
salary_date_cutoff = 0
rate_per_hour = 0
number_of_hours_per_payday = 0
number_of_hours_overtime = 0
the_number_of_absences_hours = 0
number_of_hours_of_honorarium = 0
number_of_hours_in_tardiness = 0
withholding_tax = 0
sss_contribution = 0
philhealth_contribution = 0
pagibig = 100

#Input all the needed data
print("=== Employee Salary Information ===")
company_name = input("Enter your Company Name: ")
department_of_employee = input("Enter your Department: ")
employee_codenumber = input("Enter your Code/Number: ")
employee_name = input("Enter your Name: ")
salary_date_cutoff = int(input("Enter your Salary Date Cut-off (day of the month): "))
rate_per_hour = float(input("Enter the Rate per Hour: "))
number_of_hours_per_payday = int(input("Enter the Number of Hours per Payday: "))
number_of_hours_overtime = int(input("Enter the Number of Overtime Hours: "))
the_number_of_absences_hours = int(input("Enter the Number of Absences (in hours): "))
number_of_hours_of_honorarium = int(input("Enter the Number of Honorarium Hours: "))
number_of_hours_in_tardiness = int(input("Enter the Number of Tardiness (in hours): "))

#Compute basic data
basic_pay = rate_per_hour * number_of_hours_per_payday
overtime_pay = rate_per_hour * number_of_hours_overtime
absences = rate_per_hour * the_number_of_absences_hours
honorarium = rate_per_hour * number_of_hours_of_honorarium
tardiness = rate_per_hour * number_of_hours_in_tardiness

#Compute Gross Earnings
gross_earnings = basic_pay + overtime_pay + honorarium

#Compute monthly income for sss contribution and philhealth contribution
monthly_income = gross_earnings

#Compute SSS Contribution
if monthly_income < 4250:
    sss_contribution = 180
elif 4250 <= monthly_income <= 4749.99:
    sss_contribution = 202.50
elif 4750 <= monthly_income <= 5249.99:
    sss_contribution = 225
elif 5250 <= monthly_income <= 5749.99:
    sss_contribution = 247.50
elif 5750 <= monthly_income <= 6249.99:
    sss_contribution = 270
elif 6250 <= monthly_income <= 6749.99:
    sss_contribution = 292.50
elif 6750 <= monthly_income <= 7249.99:
    sss_contribution = 315
elif 7250 <= monthly_income <= 7749.99:
    sss_contribution = 337.50
elif 7750 <= monthly_income <= 8249.99:
    sss_contribution = 360
elif 8250 <= monthly_income <= 8749.99:
    sss_contribution = 382.50
elif 8750 <= monthly_income <= 9249.99:
    sss_contribution = 405
elif 9250 <= monthly_income <= 9749.99:
    sss_contribution = 427.50
elif 9750 <= monthly_income <= 10249.99:
    sss_contribution = 450
elif 10250 <= monthly_income <= 10749.99:
    sss_contribution = 472.50
elif 10750 <= monthly_income <= 11249.99:
    sss_contribution = 495
elif 11250 <= monthly_income <= 11749.99:
    sss_contribution = 517.50
elif 11750 <= monthly_income <= 12249.99:
    sss_contribution = 540
elif 12250 <= monthly_income <= 12749.99:
    sss_contribution = 562.50
elif 12750 <= monthly_income <= 13249.99:
    sss_contribution = 585
elif 13250 <= monthly_income <= 13749.99:
    sss_contribution = 607.50
elif 13750 <= monthly_income <= 14249.99:
    sss_contribution = 630
elif 14250 <= monthly_income <= 14749.99:
    sss_contribution = 652.50
elif 14750 <= monthly_income <= 15249.99:
    sss_contribution = 675
elif 15250 <= monthly_income <= 15749.99:
    sss_contribution = 697.50
elif 15750 <= monthly_income <= 16249.99:
    sss_contribution = 720
elif 16250 <= monthly_income <= 16749.99:
    sss_contribution = 742.50
elif 16750 <= monthly_income <= 17249.99:
    sss_contribution = 765
elif 17250 <= monthly_income <= 17749.99:
    sss_contribution = 787.50
elif 17750 <= monthly_income <= 18249.99:
    sss_contribution = 810
elif 18250 <= monthly_income <= 18749.99:
    sss_contribution = 832.50
elif 18750 <= monthly_income <= 19249.99:
    sss_contribution = 855
elif 19250 <= monthly_income <= 19749.99:
    sss_contribution = 877.50
elif 19750 <= monthly_income <= 29749.99:
    sss_contribution = 900
else:
    sss_contribution = 900


#Compute PhilHealth contribution based on semi-monthly gross salary
if monthly_income <= 10000:
    philhealth_contribution = 500
elif 10001 <= monthly_income < 100000:
    philhealth_contribution = (monthly_income * 0.05)
else:
    philhealth_contribution = 5000
    
#Compute withholding tax
if gross_earnings <= 10416:
    withholding_tax = 0
elif 10417 <= gross_earnings <= 16666:
    withholding_tax = (gross_earnings - 10417) * 0.15
elif 16667 <= gross_earnings <= 33332:
    withholding_tax = 937.50 + (gross_earnings - 16667) * 0.20
elif 33333 <= gross_earnings <= 83332:
    withholding_tax = 4270.70 + (gross_earnings - 33333) * 0.25
elif 83333 <= gross_earnings <= 333332:
    withholding_tax = 16770.70 + (gross_earnings - 83333) * 0.30
else:
    withholding_tax = 91770.70 + (gross_earnings - 333333) * 0.35

# Deductions
deductions = (absences + tardiness + withholding_tax + sss_contribution + philhealth_contribution + pagibig)

# Net Pay
net_pay = gross_earnings - deductions


# Display results
print("\n=== Employee Salary Details ===")
print("=" * 40)  #Divider line

print(f"Company Name: \t\t\t{company_name}")
print(f"Department: \t\t\t{department_of_employee}")
print(f"Employee Code/Number: \t{employee_codenumber}")
print(f"Employee Name: \t\t\t{employee_name}")
print(f"Salary Date Cut-off: \t{salary_date_cutoff}")

print("\n=== Salary Breakdown ===")
print("=" * 40)  #Divider line
print(f"Rate per Hour: \t\t\t₱{rate_per_hour:.2f}")
print(f"Basic Pay: \t\t\t\t₱{basic_pay:.2f}")
print(f"Overtime Pay: \t\t\t₱{overtime_pay:.2f}")
print(f"Absences (in hours): \t{absences} hours")
print(f"Honorarium: \t\t\t₱{honorarium:.2f}")
print(f"Tardiness: \t\t\t\t{tardiness} hours")

print("\n=== Contributions and Deductions ===")
print("=" * 40)  #Divider line
print(f"Withholding Tax: \t\t\t-₱{withholding_tax:.2f}")
print(f"SSS Contribution: \t\t\t-₱{sss_contribution:.2f}")
print(f"Pag-Ibig Contribution: \t\t-₱{pagibig:.2f}")
print(f"PhilHealth Contribution: \t-₱{philhealth_contribution:.2f}")

print("\n=== Earnings Summary ===")
print("=" * 40)  #Divider line
print(f"Gross Earnings: \t\t\t₱{gross_earnings:.2f}")
print(f"Total Deductions: \t\t\t-₱{deductions:.2f}")
print(f"Net Pay: \t\t\t\t\t₱{net_pay:.2f}")

print("=" * 40)  #Final divider line