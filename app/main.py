from database import session
from models import Medication

def add_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    user = Medication(username = name, email=email)
    session.add(user)
    session.commit()
    print(f"{name} added successfully")

def list_users():
    users = session.query(Medication).all()
    if not users:
        print("No users found")
    else:
        for user in users:
            print(f"Id: {user.id}, Name: {user.name}, Email: {user.email}")

def delete_user():
    user_id = input("Enter the user Id t delete: ")
    user = session.query(Medication).filter(Medication.id == user_id).first()

    if user:
        session.delete(user)
        session.commit()
        print(f"{user.name} has been deleted successfully!")
    else:
        print("User not found")

def main():
    while True:
        print("\n***** Medication Reminder System *****")
        print("1. Add New Medication")
        print("1. View Medications")
        print("1. Check Due Medications (Reminders)")
        print("1. Mark Medication as Taken")
        print("1. View Dose History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            delete_user()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()