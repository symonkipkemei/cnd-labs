# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.
from datetime import date, datetime

class DoctorsForm:
    def __init__(self,patient_name:str,date_of_appointment:date,time_of_appointment:str,doctors_office:str,doctors_name:str,phone_number:int,speciality:str,reason_of_visit:str) -> None:
        self.patient_name=patient_name
        self.date_of_appointment=date_of_appointment
        self.time_of_appointment=time_of_appointment
        self.doctors_office=doctors_office
        self.doctors_name=doctors_name
        self.phone_number=phone_number
        self.speciality=speciality
        self.reason_of_visit=reason_of_visit

    def __str__(self) -> str:
        return f"Welcome {self.patient_name} for diagnosis of {self.reason_of_visit}.You will be attended by Dr.{self.doctors_name} on {self.date_of_appointment} at {self.doctors_office}. Thank you!"

date_of_visit = date.today()
date_of_visit = str(date_of_visit)
now = datetime.now()
time_of_visit = now.time()
time_of_visit = str(time_of_visit)


symon = DoctorsForm("symon kipkemei",date_of_visit,time_of_visit,"Kitengela medical services","Philemon too",254718454749,"bones","scrotum")

kipchumba = DoctorsForm("Bruce kipkemboi",date_of_visit,time_of_visit,"Kabarnet district hospital","diana alamata",254722686167,"kids", "ringworms on the head")

print(symon)

print(kipchumba)