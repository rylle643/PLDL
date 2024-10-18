class Employee:
    hdmf = 100.00

    def __init__(self):
        self.hmdf_contribution = 100.00
        self.company_name = input("Enter Company Name: ")
        self.employee_department = input("Enter Employee Department: ")
        self.employee_name = input("Enter Employee Name: ")
        self.employee_code = input("Enter Employee Code: ")
        self.salary_cut_off = input("Enter Cut-off Date: ")
        self.emp_rate_per_hour = float(input("Employee Rate per Hour: "))
        self.emp_num_of_hours_per_payday = int(input("Employee's Number of Hours Worked per Payday: "))
        self.emp_hour_overtime = float(input("Employee Overtime Hours: "))
        self.honorarium_pay = float(input("Employee Honorarium Pay: "))
        self.emp_num_of_absences = int(input("Employee Absences: "))
        self.emp_num_tardiness = int(input("Employee Tardiness: "))

    def emp_salary_computation(self):
        self.basic_pay = self.emp_rate_per_hour * self.emp_num_of_hours_per_payday
        self.overtime_pay = self.emp_hour_overtime * self.emp_rate_per_hour
        self.emp_gross_earnings = self.basic_pay + self.overtime_pay + self.honorarium_pay
        self.emp_absences = self.emp_num_of_absences * self.emp_rate_per_hour
        self.emp_tardiness = self.emp_num_tardiness * self.emp_rate_per_hour

    def emp_sss_contribution(self):
        ranges = [
            (0, 4249.99, 180.00),
            (4250, 4749.99, 202.50),
            (4750, 5249.99, 225.00),
            (5250, 5749.99, 247.50),
            (5750, 6249.99, 270.00),
            (6250, 6749.99, 292.50),
            (6750, 7249.99, 315.00),
            (7250, 7749.99, 337.50),
            (7750, 8249.99, 360.00),
            (8250, 8749.99, 382.50),
            (8750, 9249.99, 405.00),
            (9250, 9749.99, 427.50),
            (9750, 10249.99, 450.00),
            (10250, 10749.99, 472.50),
            (10750, 11249.99, 495.00),
            (11250, 11749.99, 517.50),
            (11750, 12249.99, 540.00),
            (12250, 12749.99, 562.50),
            (12750, 13249.99, 585.00),
            (13250, 13749.99, 607.00),
            (13750, 14249.99, 630.00),
            (14250, 14749.99, 652.50),
            (14750, 15249.99, 675.00),
            (15250, 15749.99, 697.50),
            (15750, 16249.99, 720.00),
            (16250, 16749.99, 742.50),
            (16750, 17249.99, 765.00),
            (17250, 17749.99, 787.50),
            (17750, 18249.99, 810.00),
            (18250, 18749.99, 832.50),
            (18750, 19249.99, 855.00),
            (19250, 19749.99, 877.50),
            (19750, 20249.99, 900.00),
            (20250, 24749.99, 900.00)
        ]
        for lower, upper, contribution in ranges:
            if lower <= self.emp_gross_earnings <= upper:
                self.sss_contribution = contribution
                return
        self.sss_contribution = 900.00

    def emp_philhealth_contribution(self):
        if self.emp_gross_earnings < 10000:
            self.philhealth_contribution = 0.00
        else:
            self.philhealth_contribution = self.emp_gross_earnings * 0.0450

    def emp_tax_contribution(self):
        tax_brackets = [
            (0, 10416, 0.00, 0.00),
            (10417, 16666, 0.15, 0.00),
            (16667, 33332, 0.20, 937.50),
            (33333, 83332, 0.25, 4270.70),
            (83333, 333332, 0.30, 16770.70),
            (333333, float('inf'), 0.35, 91770.70)
        ]

        for lower_bound, upper_bound, rate, base_tax in tax_brackets:
            if lower_bound <= self.emp_gross_earnings <= upper_bound:
                self.tax_contribution = (self.emp_gross_earnings - lower_bound) * rate + base_tax
                break
        else:
            self.tax_contribution = 0.00

    def emp_total_deduction(self):
        self.deduction = self.emp_absences + self.emp_tardiness + self.tax_contribution + self.sss_contribution + self.philhealth_contribution + self.hmdf_contribution

    def emp_employee_netpay(self):
        self.net_pay = self.emp_gross_earnings - self.deduction

    def emp_displayEmployee(self):
        print("Company Name: ", self.company_name)
        print("Employee Department: ", self.employee_department)
        print("Employee Name: ", self.employee_name)
        print("Employee Code: ", self.employee_code)
        print("Cut-Off Date: ", self.salary_cut_off)
        print("Basic Pay: %.2f" % self.basic_pay)
        print("Overtime Pay: %.2f" % self.overtime_pay)
        print("Gross Income: %.2f" % self.emp_gross_earnings)
        print("Absences: %.2f" % self.emp_absences)
        print("Tardiness: %.2f" % self.emp_tardiness)
        print("SSS Contribution: %.2f" % self.sss_contribution)
        print("Philhealth Contribution: %.2f" % self.philhealth_contribution)
        print("Total Deduction: %.2f" % self.deduction)
        print("Net Income: %.2f" % self.net_pay)

emp1 = Employee()
emp1.emp_salary_computation()
emp1.emp_sss_contribution()
emp1.emp_philhealth_contribution()
emp1.emp_tax_contribution()
emp1.emp_total_deduction()
emp1.emp_employee_netpay()
emp1.emp_displayEmployee()
