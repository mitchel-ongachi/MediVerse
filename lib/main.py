from db.database import SessionLocal
from db.models import Hospital, Department, Doctor, Patient, MedicalRecord, Appointment, TestResult
from datetime import datetime

def get_session():
    return SessionLocal()

# Hospital functions
def add_hospital(name, location, contact_number):
    session = get_session()
    try:
        new_hospital = Hospital(name=name, location=location, contact_number=contact_number)
        session.add(new_hospital)
        session.commit()
        print(f"Hospital '{name}' added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error adding hospital: {e}")
    finally:
        session.close()

def get_hospital(hospital_id):
    session = get_session()
    try:
        hospital = session.query(Hospital).get(hospital_id)
        if hospital:
            print(f"Hospital ID: {hospital.id}, Name: {hospital.name}, Location: {hospital.location}, Contact: {hospital.contact_number}")
        else:
            print("Hospital not found.")
    except Exception as e:
        print(f"Error retrieving hospital: {e}")
    finally:
        session.close()

# Department functions
def add_department(name, hospital_id):
    session = get_session()
    try:
        new_department = Department(name=name, hospital_id=hospital_id)
        session.add(new_department)
        session.commit()
        print(f"Department '{name}' added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error adding department: {e}")
    finally:
        session.close()

def get_department(department_id):
    session = get_session()
    try:
        department = session.query(Department).get(department_id)
        if department:
            print(f"Department ID: {department.id}, Name: {department.name}")
        else:
            print("Department not found.")
    except Exception as e:
        print(f"Error retrieving department: {e}")
    finally:
        session.close()

# Doctor functions
def add_doctor(name, specialty, department_id):
    session = get_session()
    try:
        new_doctor = Doctor(name=name, specialty=specialty, department_id=department_id)
        session.add(new_doctor)
        session.commit()
        print(f"Doctor '{name}' added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error adding doctor: {e}")
    finally:
        session.close()

def get_doctor(doctor_id):
    session = get_session()
    try:
        doctor = session.query(Doctor).get(doctor_id)
        if doctor:
            print(f"Doctor ID: {doctor.id}, Name: {doctor.name}, Specialty: {doctor.specialty}")
        else:
            print("Doctor not found.")
    except Exception as e:
        print(f"Error retrieving doctor: {e}")
    finally:
        session.close()

# Patient functions
def add_patient(name, date_of_birth, gender):
    session = get_session()
    try:
        new_patient = Patient(name=name, date_of_birth=date_of_birth, gender=gender)
        session.add(new_patient)
        session.commit()
        print(f"Patient '{name}' added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error adding patient: {e}")
    finally:
        session.close()

def get_patient(patient_id):
    session = get_session()
    try:
        patient = session.query(Patient).get(patient_id)
        if patient:
            print(f"Patient ID: {patient.id}, Name: {patient.name}, Date of Birth: {patient.date_of_birth}, Gender: {patient.gender}")
        else:
            print("Patient not found.")
    except Exception as e:
        print(f"Error retrieving patient: {e}")
    finally:
        session.close()

# Medical Record functions
def add_medical_record(patient_id, doctor_id, notes):
    session = get_session()
    try:
        new_record = MedicalRecord(patient_id=patient_id, doctor_id=doctor_id, notes=notes)
        session.add(new_record)
        session.commit()
        print("Medical record added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error adding medical record: {e}")
    finally:
        session.close()

def get_medical_record(record_id):
    session = get_session()
    try:
        record = session.query(MedicalRecord).get(record_id)
        if record:
            print(f"Record ID: {record.id}, Patient ID: {record.patient_id}, Doctor ID: {record.doctor_id}, Notes: {record.notes}")
        else:
            print("Medical record not found.")
    except Exception as e:
        print(f"Error retrieving medical record: {e}")
    finally:
        session.close()

# Appointment functions
def add_appointment(patient_id, doctor_id, appointment_date=None):
    if appointment_date is None:
        appointment_date = datetime.now()
    session = get_session()
    try:
        new_appointment = Appointment(patient_id=patient_id, doctor_id=doctor_id, appointment_date=appointment_date)
        session.add(new_appointment)
        session.commit()
        print("Appointment added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error adding appointment: {e}")
    finally:
        session.close()

def get_appointment(appointment_id):
    session = get_session()
    try:
        appointment = session.query(Appointment).get(appointment_id)
        if appointment:
            print(f"Appointment ID: {appointment.id}, Patient ID: {appointment.patient_id}, Doctor ID: {appointment.doctor_id}, Date: {appointment.appointment_date}")
        else:
            print("Appointment not found.")
    except Exception as e:
        print(f"Error retrieving appointment: {e}")
    finally:
        session.close()

# Test Result functions
def add_test_result(medical_record_id, result):
    session = get_session()
    try:
        new_test_result = TestResult(medical_record_id=medical_record_id, result=result)
        session.add(new_test_result)
        session.commit()
        print("Test result added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error adding test result: {e}")
    finally:
        session.close()

def get_test_result(test_result_id):
    session = get_session()
    try:
        test_result = session.query(TestResult).get(test_result_id)
        if test_result:
            print(f"Test Result ID: {test_result.id}, Medical Record ID: {test_result.medical_record_id}, Result: {test_result.result}")
        else:
            print("Test result not found.")
    except Exception as e:
        print(f"Error retrieving test result: {e}")
    finally:
        session.close()

def main():
    while True:
        print("\nOptions:")
        print("1. Add Hospital")
        print("2. Get Hospital")
        print("3. Add Department")
        print("4. Get Department")
        print("5. Add Doctor")
        print("6. Get Doctor")
        print("7. Add Patient")
        print("8. Get Patient")
        print("9. Add Medical Record")
        print("10. Get Medical Record")
        print("11. Add Appointment")
        print("12. Get Appointment")
        print("13. Add Test Result")
        print("14. Get Test Result")
        print("15. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter hospital name (default: St Mary): ") or "St Mary"
            location = input("Enter hospital location (default: Nairobi): ") or "Nairobi"
            contact_number = input("Enter contact number (default: 555-666): ") or "555-666"
            add_hospital(name, location, contact_number)
        
        elif choice == "2":
            hospital_id = int(input("Enter hospital ID: "))
            get_hospital(hospital_id)
        
        elif choice == "3":
            name = input("Enter department name: ")
            hospital_id = int(input("Enter hospital ID: "))
            add_department(name, hospital_id)

        elif choice == "4":
            department_id = int(input("Enter department ID: "))
            get_department(department_id)

        elif choice == "5":
            name = input("Enter doctor's name: ")
            specialty = input("Enter doctor's specialty: ")
            department_id = int(input("Enter department ID: "))
            add_doctor(name, specialty, department_id)

        elif choice == "6":
            doctor_id = int(input("Enter doctor ID: "))
            get_doctor(doctor_id)

        elif choice == "7":
            name = input("Enter patient's name: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            gender = input("Enter gender: ")
            add_patient(name, date_of_birth, gender)

        elif choice == "8":
            patient_id = int(input("Enter patient ID: "))
            get_patient(patient_id)

        elif choice == "9":
            patient_id = int(input("Enter patient ID: "))
            doctor_id = int(input("Enter doctor ID: "))
            notes = input("Enter medical notes: ")
            add_medical_record(patient_id, doctor_id, notes)

        elif choice == "10":
            record_id = int(input("Enter medical record ID: "))
            get_medical_record(record_id)

        elif choice == "11":
            patient_id = int(input("Enter patient ID: "))
            doctor_id = int(input("Enter doctor ID: "))
            appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
            add_appointment(patient_id, doctor_id, appointment_date)

        elif choice == "12":
            appointment_id = int(input("Enter appointment ID: "))
            get_appointment(appointment_id)

        elif choice == "13":
            medical_record_id = int(input("Enter medical record ID: "))
            result = input("Enter test result: ")
            add_test_result(medical_record_id, result)

        elif choice == "14":
            test_result_id = int(input("Enter test result ID: "))
            get_test_result(test_result_id)
        
        elif choice == "15":
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
