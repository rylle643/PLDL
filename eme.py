class SchoolAssessment:

    def __init__(self):
        self.student_name = ""
        self.course = ""
        self.student_number = ""
        self.academic_year = ""
        self.semester = ""
        self.year = ""
        self.printed_date = ""

    def get_student_data(self):
        self.student_name = input("Enter student's name: ")
        self.course = input("Enter course: ")
        self.student_number = input("Enter student number: ")
        self.academic_year = input("Enter academic year (e.g., 2022-2023): ")
        self.semester = input("Enter semester (e.g., 1st, 2nd): ")
        self.year = input("Enter year level (e.g., Second Year): ")
        self.printed_date = input("Enter printed date (e.g., MM/DD/YYYY): ")

    def display_basic_data(self):
        print("-" * 120)
        print(f"{'OFFICE OF THE REGISTRAR':>120}")
        print("\n")
        print(f"{'CERTIFICATE OF ENROLLMENT':^120}")
        print(f"{self.semester} Semester, {self.academic_year}".center(120))
        print("\n")
        print(f"\t\t\t\t{'NAME':<10}: {self.student_name:<50}    {'STUDENT NO.':<15}: {self.student_number}")
        print(f"\t\t\t\t{'COURSE':<10}: {self.course:<50}    {'ACAD. YEAR':<15}: {self.academic_year}")
        print("\n" + "=" * 120)


class SubjectInfo:
    def __init__(self):
        self.section = ""
        self.subject = []
        self.units = ""

    def get_subjectinfo(self, section, subject, units):
        self.section = section
        self.subject = subject
        self.units = units
        self.totalunits = 0

    def input_subjectinfo(self):
        self.subjects = []
        self.totalunits = 0
        while True:
            subject = input("Enter a subject (type 'done' to finish): ")
            if subject.lower() == 'done':
                break
            section = input("Enter section: ")
            units = int(input("Enter units: "))
            self.subjects.append({"subject": subject, "section": section, "units": units})
            self.totalunits += units
        return self.subjects

    def get_total_units(self):
        return self.totalunits

    def display_subjectinfo(self):
        return [
            f"{info['section']:<15}{info['subject']:<25}{info['units']:<5}"
            for info in self.subjects
        ]


class AssessmentOfFees:
    def __init__(self):
        self.tuition_fee = 0
        self.total_units = 0
        self.chronicle = float(input("Enter the Chronicle fee: "))
        self.athletic = float(input("Enter the Athletic fee: "))
        self.audio_visual_library = float(input("Enter the Audio-Visual Library fee: "))
        self.sg = float(input("Enter student government fee: "))
        self.cultural_fee = float(input("Enter Cultural fee: "))
        self.energy_cost_aircon = float(input("Enter Energy Cost Aircon Classroom fee: "))
        self.guidance = float(input("Enter Guidance fee: "))
        self.insurance_fee = float(input("Enter Insurance fee: "))
        self.lms = float(input("Enter Learning Management System fee: "))
        self.library_fee = float(input("Enter Library fee: "))
        self.medical_dental = float(input("Enter Medical and Dental fee: "))
        self.registration = float(input("Enter Registration fee: "))
        self.rso = float(input("Enter RSO fee: "))
        self.student_activity = float(input("Enter Student Activities fee: "))
        self.student_nurturance = float(input("Enter Student Nurturance fee: "))
        self.technology_fee = float(input("Enter Technology fee: "))
        self.test_papers = float(input("Enter Test Papers fee: "))
        self.downpayment = float(input("Enter downpayment: "))
        self.prelims = float
        self.midterms = float
        self.finals = float

    def set_total_units(self, total_units):
        self.total_units = total_units

    def get_assessment_amount(self):
        self.tuition_fee = self.total_units * 1551
        self.assessment_amount = (
            self.tuition_fee +
            self.chronicle +
            self.athletic +
            self.audio_visual_library +
            self.sg +
            self.cultural_fee +
            self.energy_cost_aircon +
            self.guidance +
            self.insurance_fee +
            self.lms +
            self.library_fee +
            self.medical_dental +
            self.registration +
            self.rso +
            self.student_activity +
            self.student_nurturance +
            self.technology_fee +
            self.test_papers
        )
        return self.assessment_amount

    def get_Schedule_of_Payment(self):
        remaining_balance = self.get_assessment_amount() - self.downpayment
        self.prelims = remaining_balance / 3
        self.midterms = self.prelims
        self.finals = self.prelims

    def display_assessment(self):
        fee_lines = [
            f"{'TUITION FEE':<30}{self.tuition_fee:>10,.2f}",
            f"{'CHRONICLE':<30}{self.chronicle:>10,.2f}",
            f"{'ATHLETIC':<30}{self.athletic:>10,.2f}",
            f"{'AUDIO-VISUAL LIBRARY':<30}{self.audio_visual_library:>10,.2f}",
            f"{'SG':<30}{self.sg:>10,.2f}",
            f"{'CULTURAL FEE':<30}{self.cultural_fee:>10,.2f}",
            f"{'ENERGY COST, AIRCON CLASSROOM':<30}{self.energy_cost_aircon:>10,.2f}",
            f"{'GUIDANCE':<30}{self.guidance:>10,.2f}",
            f"{'INSURANCE FEE':<30}{self.insurance_fee:>10,.2f}",
            f"{'LEARNING MANAGEMENT SYSTEM':<30}{self.lms:>10,.2f}",
            f"{'LIBRARY FEE':<30}{self.library_fee:>10,.2f}",
            f"{'MEDICAL AND DENTAL':<30}{self.medical_dental:>10,.2f}",
            f"{'REGISTRATION':<30}{self.registration:>10,.2f}",
            f"{'RSO':<30}{self.rso:>10,.2f}",
            f"{'STUDENT ACTIVITIES FEE':<30}{self.student_activity:>10,.2f}",
            f"{'STUDENT NURTURANCE FEE':<30}{self.student_nurturance:>10,.2f}",
            f"{'TECHNOLOGY FEE':<30}{self.technology_fee:>10,.2f}",
            f"{'TEST PAPERS':<30}{self.test_papers:>10,.2f}",
            "-" * 45,
            f"{'Assessment Amt.':<30}{self.get_assessment_amount():>10,.2f}",
            f"{'Downpayment:':<30}{self.downpayment:>10,.2f}",
            "-" * 45,
            f"{'Total Due:':<30}{self.get_assessment_amount() - self.downpayment:>10,.2f}",
            "-" * 45,
            f"|{'Schedule of Payment':^43}|",
            f"|{'of outstanding balance':^43}|",
            f"|{'after downpayment prior to:':^43}|",
            f"| {'PRELIMS':<28}{self.prelims:>13,.2f} |",
            f"| {'MIDTERMS':<28}{self.midterms:>13,.2f} |",
            f"| {'FINALS':<28}{self.finals:>13,.2f} |",
            "-" * 45,
            "*There will be a 6% surcharge p.a. for late payment.",
            "-" * 45,
            "THIS IS A TEMPORARY ASSESSMENT",
            "-" * 45,
        ]
        return fee_lines

