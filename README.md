# 💊 Medication Reminder System (CLI-Based)

## Overview

The **Medication Reminder System** is a command-line interface (CLI) application that allows users to manage and track their medication schedules, mark doses as taken, and maintain a history of their treatment logs. It is particularly helpful for individuals (especially the elderly or chronically ill) who need a simple, offline method to stay on top of their prescriptions.

---

## ✨ Features

- ✅ Add and manage users
- 💊 Add medications, dosages, and frequencies
- ⏰ Get reminders for upcoming doses
- 📅 Mark doses as taken
- 📜 View history of taken, missed, or pending doses
- 🗃️ All data is stored persistently using a MySQL database

---

## 🛠️ Tech Stack

| Layer         | Technology             |
| ------------- |------------------------|
| Language      | Python 3.12            |
| Database      | MySQL                  |
| ORM           | SQLAlchemy             |
| Migrations    | Alembic                |
| CLI Input     | `input()` + print      |
| Virtual Env   | `venv` or `virtualenv` |

---

## 📂 Project Structure
```bash
Medication-Reminder-System-CLI/
│
├── app/
│ ├── main.py # Main CLI interface
│ ├── models.py # SQLAlchemy ORM models
│ ├── database.py # DB engine and session setup
│ └── utils.py
├── migrations/ # Alembic migration files
│ ├── versions/
│ ├── env.py
│ └── script.py.mako
│
├── virtual/
├── .env 
├── .gitignore
├── alembic.ini
├── requirements.txt 
└── README.md 
```


---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/theMungai/Medication-Reminder-System-CLI.git
cd Medication-Reminder-System-CLI
```
### 2. Create and Activate Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
#### Create a .env file at the project root:
```bash
DB_USER=root
DB_PASS=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=Medication_Reminder_System
```

### 5. Run Alembic Migrations
```bash
alembic upgrade head
This will create the required tables in your MySQL database.
```

## ▶️ Running the Application
```bash
python app/main.py
```

#### You will see a CLI menu like:

```bash
***** Medication Reminder System *****
1. Add New User

2. Add New Medication

3. View Medications

4. Check Due Medications (Reminders)

5. Mark Medication as Taken

6. View Dose History

7. Exit

```

# 📘 How to Use
### 1. Add a User
You'll be asked to enter:
 - Name
 - Age

### 2. Add Medication
You'll be asked for:
 - User ID
 - Medication name (e.g. "Paracetamol")
 - Dosage (e.g. "500mg")
 - Frequency in hours (e.g. every 8 hours → enter 8)
 - Start and end dates (e.g. 2025-05-28 to 2025-06-04)
 - Times per day (e.g. 08:00, 14:00, etc.)

### 3. View Medications
See a list of all added medications and their schedules.

### 4. Check Reminders
The app checks which doses are due or missed at the current time.

### 5. Mark as Taken
You will need to enter the DoseLog ID shown in reminders/history to mark that dose as taken.

### 6. View Dose History
Shows:
 - Scheduled time
 - Status: taken, missed, or pending
 - Time actually taken (if any)

### 📌 Example Input
```bash
Enter your name: Jane Doe

Enter your age: 60

Enter user ID: 1

Medication name: Amoxicillin

Dosage: 500mg

Frequency in hours: 8

Start date: 2025-05-28

End date: 2025-06-04

Enter time for dose #1 (HH:MM): 08:00

Add another time? (y/n): y

Enter time for dose #2 (HH:MM): 16:00

Add another time? (y/n): n

```
## ⚙️ Developer Notes
 - Alembic autogeneration uses SQLAlchemy models in models.py
 - The dose_logs table automatically generates reminders based on medication frequency
 - Use alembic revision --autogenerate -m "message" to update schema changes

## ❓ FAQs
### Q: Why do I get "Dose not found" when marking as taken?
Make sure you've first run "Check Due Medications" (option 4) to generate and view DoseLog IDs.

### Q: Where can I find the DoseLog ID?
The ID is printed in option 4 or 6 when you check reminders or history.

## 🤝 Contribution
Pull requests are welcome! Please open an issue first to discuss any major changes.