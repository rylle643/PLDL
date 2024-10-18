import payroll_oop2

employee_payroll = payroll_oop2.Employee_Salary()
emp_rate_per_hour = float(input("Enter Value for Rate per Hour: "))
emp_num_of_absences = int(input("Enter value for number of absences: "))
tardiness_hours = int(input("Enter number of tardiness: "))

absences_deduction = employee_payroll.get_absences_deduction(emp_rate_per_hour, emp_num_of_absences)
tardiness_hours = employee_payroll.get_tardiness_deduction(emp_rate_per_hour, tardiness_hours)

partial_deduction = absences_deduction + tardiness_hours
print("Employee Partial Deduction: %.2f" % partial_deduction)
