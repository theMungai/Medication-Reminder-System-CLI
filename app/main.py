from database import session
from models import User, Medication, DoseLog
from datetime import datetime
from utils import generate_dose_logs

def add_user():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")

    user = User(name=name, age=age, email=email)
    session.add(user)
    session.commit()

    print(f"Id: {user.id}, Name: {user.name}, Age: {user.age} years old, Email: {user.email}")
    print(f"{user.name} added successfully.")


def add_medication():
    user_id = int(input("Enter user ID: "))
    user = session.query(User).filter_by(id=user_id).first()

    if not user:
        print("User not found.")
        return

    name = input("Enter medication name: ")
    dosage = input("Enter dosage (e.g., 500mg): ")
    frequency = int(input("Enter frequency in hours: "))
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD) or leave blank: ")

    medication = Medication(
        user_id=user.id,
        name=name,
        dosage=dosage,
        frequency_hours=frequency,
        start_date=datetime.strptime(start_date, "%Y-%m-%d").date(),
        end_date=datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else None
    )

    session.add(medication)
    session.commit()

    # 🔁 Generate dose logs now
    generate_dose_logs(medication)

    print(f"Medication '{name}' added and dose schedule generated.\n")



def view_medications():
    meds = session.query(Medication).all()
    if not meds:
        print("No medications found.")
        return
    for med in meds:
        print(f"ID: {med.id}, User ID: {med.user_id}, Name: {med.name}, Dosage: {med.dosage}, Frequency: {med.frequency_hours}h, Start: {med.start_date}, End: {med.end_date}")

def check_due_medications():
    now = datetime.now()
    due_meds = session.query(DoseLog).filter(DoseLog.scheduled_datetime <= now, DoseLog.status == 'pending').all()
    if not due_meds:
        print("No medications due right now.")
        return
    for dose in due_meds:
        med = dose.medication
        print(f"Dose ID: {dose.id}, Medication: {med.name}, Scheduled for: {dose.scheduled_datetime}")

def mark_medication_taken():
    dose_id = input("Enter DoseLog ID to mark as taken: ")
    dose = session.query(DoseLog).filter(DoseLog.id == dose_id).first()
    if not dose:
        print("Dose not found.")
        return
    if dose.status == 'taken':
        print("Dose already marked as taken.")
        return
    dose.status = 'taken'
    dose.actual_datetime = datetime.now()
    session.commit()
    print(f"Dose {dose_id} marked as taken.")

def view_dose_history():
    doses = session.query(DoseLog).order_by(DoseLog.scheduled_datetime.desc()).all()
    if not doses:
        print("No dose history found.")
        return
    for dose in doses:
        med = dose.medication
        print(f"Dose ID: {dose.id}, Medication: {med.name}, Scheduled: {dose.scheduled_datetime}, Status: {dose.status}, Taken at: {dose.actual_datetime}")

def main():
    while True:
        print("\n***** Medication Reminder System *****")
        print("1. Add New User")
        print("2. Add New Medication")
        print("3. View Medications")
        print("4. Check Due Medications (Reminders)")
        print("5. Mark Medication as Taken")
        print("6. View Dose History")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            add_medication()
        elif choice == "3":
            view_medications()
        elif choice == "4":
            check_due_medications()
        elif choice == "5":
            mark_medication_taken()
        elif choice == "6":
            view_dose_history()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
