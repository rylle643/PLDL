#Create class
class SchoolAssessment:

#Input needed data
    def __init__(self):
        self.student_name = ""
        self.course = ""
        self.student_number = ""
        self.academic_year = ""
        self.current_day = ""
        self.section = ""
        self.subject = []
        self.units = ""

    def get_student_data(self, student_name, course, student_number, academic_year, current_day, section, subject, units):
        self.student_name = student_name
        self.course = course
        self.student_number = student_number
        self.academic_year = academic_year
        self.current_day = current_day
        self.section = section
        self.subject = subject
        self.units = units

    def display_basic_data(self):
        print("Name: ", self.student_name)
        print("Course: ", self.course)
        print("Student Number: ", self.student_number)
        print("Academic Year: ", self.academic_year)

    def display_subjectinfo(self):
        print("Section \tSubject \tUnits")
        print("=" * 35)
        for info in self.subjects:
            print(f"{info['section']} \t\t{info['subject']} \t\t{info['units']}")

    def input_subjectinfo(self):
        self.subjects = []
        while True:
            subject = input("Enter a subject (type 'done' to finish): ")
            if subject.lower() == 'done':
                break
            section = input("Enter section: ")
            units = input("Enter units: ")
            self.subjects.append({"subject":subject, "section":section, "units":units})
        return self.subjects

class AssessmentOfFees:

    def __init__(self):
        self.chronicle = float(input("Enter the chronicle fee: "))
        self.athletic = float(input("Enter atheletic fee:"))
        self.audio_visual_library = float(input("Enter the audio-visual library fee: "))
        self.sg = float(input("Enter student government fee:"))
        self.cultural_fee = float(input("Enter Cultural fee fee:"))
        self.energy_cost_aircon = float(input("Enter energy cost aircon classroom fee:"))
        self.guidance = float(input("Enter guidance fee:"))
        self.insurance_fee = float(input("Enter insurance fee fee:"))
        self.lms = float(input("Enter learning management system fee:"))
        self.library_fee = float(input("Enter library fee:"))
        self.medical_dental = float(input("Enter medical and dental fee:"))
        self.registration = float(input("Enter registration fee:"))
        self.rso = float(input("Enter RSO fee:"))
        self.student_activity = float(input("Enter student activities fee:"))
        self.student_nurturane = float(input("Enter student nurturance fee:"))
        self.technology_fee = float(input("Enter technology fee:"))
        self.test_papers = float(input("Enter test papers fee:"))

    def get_AssessmentAmount(self):
        self.assessment_amount = self.cultural_fee + self.athletic + self.audio_visual_library +self.sg +self.cultural_fee + self.energy_cost_aircon + self.guidance +self.insurance_fee +self.lms +self

schoolassessment = SchoolAssessment()
schoolassessment.input_subjectinfo()
schoolassessment.display_subjectinfo()