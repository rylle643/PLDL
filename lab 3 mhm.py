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
company_name = input("Enter your Company Name: ")
department_of_employee = input("Enter your Department: ")
employee_codenumber = input("Enter your Code/Number: ")
employee_name = input("Enter your name: ")
salary_date_cutoff = int(input("Enter your salary date cut-off: "))
rate_per_hour = float(input("Enter the rate per hour: "))
number_of_hours_per_payday = int(input("Enter the number of hours per payday: "))
number_of_hours_overtime = int(input("Enter the number of overtime hours: "))
the_number_of_absences_hours = int(input("Enter the number of absences (in hours): "))
number_of_hours_of_honorarium = int(input("Enter the number of honorarium hours: "))
number_of_hours_in_tardiness = int(input("Enter the number of tardiness (in hours): "))

#Compute basic data
basic_pay = rate_per_hour * number_of_hours_per_payday
overtime_pay = rate_per_hour * number_of_hours_overtime
absences = rate_per_hour * the_number_of_absences_hours
honorarium = rate_per_hour * number_of_hours_of_honorarium
tardiness = rate_per_hour * number_of_hours_in_tardiness

#Compute Gross Earnings
gross_earnings = basic_pay + overtime_pay + honorarium

#Compute monthly income for sss contribution and philhealth contribution
monthly_income = gross_earnings * 2

#Compute SSS Contribution
if monthly_income < 4250:
    sss_contribution = 180 / 2
elif 4250 <= monthly_income <= 4749.99:
    sss_contribution = 202.50 / 2
elif 4750 <= monthly_income <= 5249.99:
    sss_contribution = 225 / 2
elif 5250 <= monthly_income <= 5749.99:
    sss_contribution = 247.50 / 2
elif 5750 <= monthly_income <= 6249.99:
    sss_contribution = 270 / 2
elif 6250 <= monthly_income <= 6749.99:
    sss_contribution = 292.50 / 2
elif 6750 <= monthly_income <= 7249.99:
    sss_contribution = 315 / 2
elif 7250 <= monthly_income <= 7749.99:
    sss_contribution = 337.50 / 2
elif 7750 <= monthly_income <= 8249.99:
    sss_contribution = 360 / 2
elif 8250 <= monthly_income <= 8749.99:
    sss_contribution = 382.50 / 2
elif 8750 <= monthly_income <= 9249.99:
    sss_contribution = 405 / 2
elif 9250 <= monthly_income <= 9749.99:
    sss_contribution = 427.50 / 2
elif 9750 <= monthly_income <= 10249.99:
    sss_contribution = 450 / 2
elif 10250 <= monthly_income <= 10749.99:
    sss_contribution = 472.50 / 2
elif 10750 <= monthly_income <= 11249.99:
    sss_contribution = 495 / 2
elif 11250 <= monthly_income <= 11749.99:
    sss_contribution = 517.50 / 2
elif 11750 <= monthly_income <= 12249.99:
    sss_contribution = 540 / 2
elif 12250 <= monthly_income <= 12749.99:
    sss_contribution = 562.50 / 2
elif 12750 <= monthly_income <= 13249.99:
    sss_contribution = 585 / 2
elif 13250 <= monthly_income <= 13749.99:
    sss_contribution = 607.50 / 2
elif 13750 <= monthly_income <= 14249.99:
    sss_contribution = 630 / 2
elif 14250 <= monthly_income <= 14749.99:
    sss_contribution = 652.50 / 2
elif 14750 <= monthly_income <= 15249.99:
    sss_contribution = 675 / 2
elif 15250 <= monthly_income <= 15749.99:
    sss_contribution = 697.50 / 2
elif 15750 <= monthly_income <= 16249.99:
    sss_contribution = 720 / 2
elif 16250 <= monthly_income <= 16749.99:
    sss_contribution = 742.50 / 2
elif 16750 <= monthly_income <= 17249.99:
    sss_contribution = 765 / 2
elif 17250 <= monthly_income <= 17749.99:
    sss_contribution = 787.50 / 2
elif 17750 <= monthly_income <= 18249.99:
    sss_contribution = 810 / 2
elif 18250 <= monthly_income <= 18749.99:
    sss_contribution = 832.50 / 2
elif 18750 <= monthly_income <= 19249.99:
    sss_contribution = 855 / 2
elif 19250 <= monthly_income <= 19749.99:
    sss_contribution = 877.50 / 2
elif 19750 <= monthly_income <= 29749.99:
    sss_contribution = 900 / 2
else:
    sss_contribution = 900 / 2


#Compute PhilHealth contribution based on semi-monthly gross salary
if monthly_income <= 10000:
    philhealth_contribution = 500 / 2
elif 10001 <= monthly_income < 100000:
    philhealth_contribution = (monthly_income * 0.05) / 2
else:
    philhealth_contribution = 5000 / 2

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

width = 100

print("=" * width)

# Display results
print("\n--- Employee Salary Details ---")
print("Company Name:" ,company_name)
print("Department:" ,department_of_employee)
print("Employee Code/Number:" ,employee_codenumber)
print("Employee Name:" ,employee_name)
print("Salary Date Cut-off:" ,salary_date_cutoff)
print("Rate per hour:" ,rate_per_hour)
print("Basic Pay:" , basic_pay)
print("Overtime Pay:" ,overtime_pay)
print("Absences:" ,absences)
print("Honorarium:" ,honorarium)
print("Tardiness:" ,tardiness)
print("Withholding Tax:" ,withholding_tax)
print("SSS Contribution:" ,sss_contribution)
print("Pag-Ibig Contribution:" ,pagibig)
print("PhilHealth Contribution:" ,philhealth_contribution)
print("Gross Earnings:" ,gross_earnings)
print("Total Deductions:" ,deductions)
print("Net Pay:" ,net_pay)

print("=" * width)