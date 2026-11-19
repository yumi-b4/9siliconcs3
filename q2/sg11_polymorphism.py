# Creates a class called Patient, this is our parent class
class Patient:
# the constructor lets it automatically runs whenever we create a new patient object
    def __init__(self, name, bill_amount):
# saves the patient's name and bill amount inside the object
        self.name = name
        self.bill_amount = bill_amount
# creates a method called calculate_bill() which sends the result back 
    def calculate_bill(self):
        return self.bill_amount
# this is the default method that children can override
    def display_patient_type(self):
        print("Patiend Type: Regular Patient")

# creates a class called SeniorPatient, which inherits the parents attributes and methods 
class SeniorPatient(Patient):
# creates a method called calculate_bill() which sends the result back 
    def calculate_bill(self):
# calls the parent class' calculate_bill() method and multiplies it by 0.80 to give a 20% discount 
        return super().calculate_bill() * 0.80
# overrides the parent's display_patient_type()
    def display_patient_type(self):
        print("Patient Type: Senior Citizen")

# creates another child class calls PhilHealthPatient
class PhilHealthPatient(Patient):
# creates its own version of the parents method, calculate_bill()
    def calculate_bill(self):
# calls the parent class' calculate_bill() method and multiplies it by 0.85 to give a 15% discount 
        return super().calculate_bill() * 0.85
# overrides the parent's display_patient_type()
    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")

# creates objects 
patient1 = Patient("Rob", 10000)
patient2 = SeniorPatient("Naomi", 10000)
patient3 = PhilHealthPatient("Reen", 10000)

# putting the objects in a list, which allows us to process all patients using one loop
patients = [patient1, patient2, patient3]

# the loop goes through each patient in the list 
for patient in patients:
# calls the display_patient_type() method of the current object
    print("Patient Name:", patient.name)
# calls the calculate_bill() method and prints the final bill
    patient.display_patient_type()
    print("Final Bill: ₱", patient.calculate_bill())
