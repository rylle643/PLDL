class InputData:

#Input all the needed data
    def __init__(self):
        self.name = ""
        self.house_no = ""
        self.brgy = ""
        self.city = ""
        self.province = ""
        self.can = ""
        self.type = ""
        self.due = ""
        self.rate = 0
        self.consumption = 0
        self.charges = 0
        self.gen = 0
        self.tran = 0
        self.sl = 0
        self.distribution = 0
        self.sub = 0
        self.gov = 0
        self.univ_charges = 0
        self.fit = 0
        self.applied = 0
        self.other = 0
        self.installment = 0
        self.total_amt = 0
        self.balance = 0
        self.balance_output = ""
        self.meter_reading_date = ""
        self.bill_period = ""
        self.current_reading = 0
        self.next_meter_reading = ""
#Let the user put the needed data
    def input_data(self):
        self.name = input("Enter name: ")
        self.house_no = input("Enter house/block/lot no.: ")
        self.brgy = input("Enter barangay: ")
        self.city = input("Enter city: ")
        self.province = input("Enter province: ")
        self.can = input("Enter customer account number: ")
        self.type = input("Choose customer type [Residential/Commercial]:")
        self.due = input("Enter bill due date: ")
        self.rate = float(input("Enter rate (per kWh): "))
        self.consumption = float(input("Enter actual consumption: "))
        self.gen = float(input("Enter Generation amount: "))
        self.tran = float(input("Enter Transmission amount: "))
        self.sl = float(input("Enter System Loss amount: "))
        self.distribution = float(input("Enter Distribution(Meralco) amount: "))
        self.sub = float(input("Enter Subsidies amount: "))
        self.gov = float(input("Enter Government Taxes amount: "))
        self.univ_charges = float(input("Enter Universal Charges amount: "))
        self.fit = float(input("Enter FIT-All (Renewable) amount: "))
        self.applied = float(input("Enter Applied Credits amount: "))
        self.other = float(input("Enter Other Charges: "))
        self.installment = float(input("Enter Installment Due amount: "))
        self.balance = float(input("Enter balance: "))
        self.meter_reading_date = input("Enter date of meter reading: ")
        self.bill_period = input("Enter bill period: ")
        self.current_reading = float(input("Enter current reading: "))
        self.next_meter_reading = input("Enter next meter reading date: ")
#Make a condition for the balance
    def check_balance(self):
        if self.balance == 0:
            self.balance_output = "Thank You"
        elif self.balance > 0:
            self.balance_output = "Kindly Pay"
#Compute the total amount
    def compute_amtdue(self):
        self.charges = self.rate * self.consumption
        self.total_amt = (
            self.charges +
            self.gen +
            self.tran +
            self.sl +
            self.distribution +
            self.sub +
            self.gov +
            self.univ_charges +
            self.fit +
            self.applied +
            self.other +
            self.installment
        )
#Create display info
    def display_info(self):
        print("\n", self.name,
              "\n", self.house_no,
              "\n", self.brgy,
              "\n", self.city,
              "\n", self.province)
#Create display summary
    def display_summary(self):
        fee_lines = [
            "\n",
            "+" + "=" * 70 + "+",
            f"| {'Summary for Customer Account Number (CAN):':<44}{self.can:<24} |",
            "+" + "=" * 70 + "+",
            f"| {'Balance from previous billing:':<39}{'Balance status:':<29} |",
            f"| {self.balance:<44,.2f}{self.balance_output:<24} |",
            "+" + "-" * 70 + "+"
        ]
        for line in fee_lines:
            print(line)
#Display Service
    def display_serviceinfo(self):
        fee_lines = [
            "\n",
            "+" + "=" * 70 + "+",
            f"| {'Service Info ':<44}{' ':<24} |",
            "+" + "=" * 70 + "+",
            f"| {'Service ID Number: ':<39}{self.can:<29} |",
            "+" + "-" * 70 + "+",
            f"| {'Type: ':<39}{self.type:<29} |",
            "+" + "-" * 70 + "+",
            f"| {'Name: ':<39}{self.name:<29} |",
            "+" + "-" * 70 + "+",
            f"| {'Service Address: ':<20}{self.house_no}, {self.brgy}, {self.city}, {self.province:<39} |",
            "+" + "-" * 70 + "+"
        ]
        for line in fee_lines:
            print(line)
#Display Billing info
    def display_billinginfo(self):
        fee_lines = [
            "\n",
            "+" + "=" * 70 + "+",
            f"| {'Billing Info ':<44}{' ':<24} |",
            "+" + "=" * 70 + "+",
            f"| {'Date of Meter Reading: ':<39}{self.meter_reading_date:<29} |",
            "+" + "-" * 70 + "+",
            f"| {'Bill Period: ':<39}{self.bill_period:<29} |",
            "+" + "-" * 70 + "+",
            f"| {'Due Date: ':<39}{self.due:<29} |",
            "+" + "-" * 70 + "+",
            f"| {'Total kWh: ':<39}{self.consumption:<29} |",
            "+" + "-" * 70 + "+",
            f"| {'Current reading: ':<39}{self.current_reading:<29} |",
            "+" + "-" * 70 + "+",
            f"| {'Next meter reading: ':<39}{self.next_meter_reading:<29} |",
            "+" + "-" * 70 + "+"
        ]
        for line in fee_lines:
            print(line)
#Display CAN
    def display_can(self):
        fee_lines = [
            "\n"
            "+" + "=" * 70 + "+",
            f"| {'Customer Account Number (CAN):':<34}{'Due Date:':<33}  |",
            f"| {self.can:<34}{self.bill_period:<34} |",
            "+" + "=" * 70 + "+",
        ]
        for line in fee_lines:
            print(line)
#Display Billing Sum
    def display_billsum(self):
        fee_lines = [
            "\n"
            "+" + "=" * 70 + "+",
            f"| {'Billing Info ':<44}{' ':<24} |",
            "+" + "=" * 70 + "+",
            f"| {'Remaining Balance: ':<39}{self.balance:<29} |",
            f"| {' ':<39}{' ':<29} |",
            f"| {'Charges for this billing: ':<39}{self.charges:<29} |",
            f"| {'Generation: ':<39}{self.gen:<29} |",
            f"| {'Transmission: ':<39}{self.tran:<29} |",
            f"| {'System Loss: ':<39}{self.sl:<29} |",
            f"| {'Distribution (Meralco): ':<39}{self.distribution:<29} |",
            f"| {'Subsidies: ':<39}{self.sub:<29} |",
            f"| {'Government Taxes: ':<39}{self.gov:<29} |",
            f"| {'Universal Charges: ':<39}{self.univ_charges:<29} |",
            f"| {'Fit-All: ':<39}{self.fit:<29} |",
            f"| {'Applied Credits: ':<39}{self.applied:<29} |",
            f"| {'Other Charges: ':<39}{self.other:<29} |",
            f"| {'Installment Due: ':<39}{self.installment:<29} |",
            "+" + "-" * 70 + "+",
            f"| {'Total Amount Dues: ':<39}{self.total_amt:<29} |",
            "+" + "=" * 70 + "+",
        ]
        for line in fee_lines:
            print(line)


summary = InputData()
summary.input_data()
summary.compute_amtdue()
summary.check_balance()
summary.display_info()
summary.display_summary()
summary.display_serviceinfo()
summary.display_billinginfo()
summary.display_can()
summary.display_billsum()


