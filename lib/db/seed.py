# lib/db/seed.py
from .database import init_db, SessionLocal
from .models import Hospital, Department, Doctor, Patient


def populate():
    init_db()

    session = SessionLocal()
    try:
        hospital = Hospital(name="St Mary", location="Nairobi", contact_number="555-666")
        session.add(hospital)
        session.commit()

        department = Department(name="Cardiology", hospital_id=hospital.id)
        session.add(department)
        session.commit()

        doctor = Doctor(name="Dr. John Doe", specialty="Cardiologist", department_id=department.id)
        session.add(doctor)
        session.commit()

        
        patient = Patient(name="Jane Smith")
        session.add(patient)
        session.commit()

        print("Sample data populated.")
    except Exception as e:
        print(f"Error populating database: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    populate()
