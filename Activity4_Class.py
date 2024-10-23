#Create class
class SchoolAssessment:

#Input needed data
    def __init__(self):
        self.student_name = ""
        self.course = ""
        self.student_number = ""
        self.academic_year = ""
        self.current_day = ""

    def get_student_data(self, student_name, course, student_number, academic_year, current_day):
        self.student_name = student_name
        self.course = course
        self.student_number = student_number
        self.academic_year = academic_year
        self.current_day = current_day

    def display_basic_data(self):
        print("Name: ", self.student_name)
        print("Course: ", self.course)
        print("Student Number: ", self.student_number)
        print("Academic Year: ", self.academic_year)

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
        self.totalunits=0
        while True:
            subject = input("Enter a subject (type 'done' to finish): ")
            if subject.lower() == 'done':
                break
            section = input("Enter section: ")
            units = int(input("Enter units: "))
            self.subjects.append({"subject":subject, "section":section, "units":units})
            self.totalunits += units
        return self.subjects

    def get_total_units(self):
        return self.totalunits

    def display_subjectinfo(self):
        print(f"{'Section':<15}{'Subject':<25}{'Units':<5}")
        print("=" * 60)
        for info in self.subjects:
            print(f"{info['section']:<15}{info['subject']:<25}{info['units']:<5}")
        print(f"\n{'Total Units:':<40}{self.totalunits:<5}")

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

    def display_assessment(self):
        print("\n")
        print("-" * 45)
        print("\t\t\tASSESSMENT OF FEES")
        print("-" * 45)
        print(f"{'TUITION FEE':<30}{self.tuition_fee:>10,.2f}")
        print(f"{'CHRONICLE':<30}{self.chronicle:>10,.2f}")
        print(f"{'ATHLETIC':<30}{self.athletic:>10,.2f}")
        print(f"{'AUDIO-VISUAL LIBRARY':<30}{self.audio_visual_library:>10,.2f}")
        print(f"{'SG':<30}{self.sg:>10,.2f}")
        print(f"{'CULTURAL FEE':<30}{self.cultural_fee:>10,.2f}")
        print(f"{'ENERGY COST, AIRCON CLASSROOM':<30}{self.energy_cost_aircon:>10,.2f}")
        print(f"{'GUIDANCE':<30}{self.guidance:>10,.2f}")
        print(f"{'INSURANCE FEE':<30}{self.insurance_fee:>10,.2f}")
        print(f"{'LEARNING MANAGEMENT SYSTEM':<30}{self.lms:>10,.2f}")
        print(f"{'LIBRARY FEE':<30}{self.library_fee:>10,.2f}")
        print(f"{'MEDICAL AND DENTAL':<30}{self.medical_dental:>10,.2f}")
        print(f"{'REGISTRATION':<30}{self.registration:>10,.2f}")
        print(f"{'RSO':<30}{self.rso:>10,.2f}")
        print(f"{'STUDENT ACTIVITIES FEE':<30}{self.student_activity:>10,.2f}")
        print(f"{'STUDENT NURTURANCE FEE':<30}{self.student_nurturance:>10,.2f}")
        print(f"{'TECHNOLOGY FEE':<30}{self.technology_fee:>10,.2f}")
        print(f"{'TEST PAPERS':<30}{self.test_papers:>10,.2f}\n")
        print("-" * 45)
        print(f"{'Assessment Amt.':<30}{self.get_assessment_amount():>10,.2f}")
        print(f"{'Downpayment:':<30}{self.downpayment:>10,.2f}")
        print(f"{'Total Due:':<30}{self.get_assessment_amount() - self.downpayment:>10,.2f}")
        print("-" * 45)




#subject = SubjectInfo()
#subject.input_subjectinfo()
#subject.display_subjectinfo()

#subject = SubjectInfo()
#.input_subjectinfo()
#totalunits = subject.get_total_units()
#assessment = AssessmentOfFees()
#assessment.set_total_units(totalunits)
#assessment.get_assessment_amount()
#assessment.display_assessment()





