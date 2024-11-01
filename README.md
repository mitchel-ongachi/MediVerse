# MediVerse: Medical Data Collection & Analysis Platform

MediVerse is a Command-Line Interface (CLI) application that simplifies and centralizes hospital data management. Designed for healthcare settings, MediVerse streamlines the collection, storage, and analysis of medical information to enhance data accessibility, patient care, and decision-making.

---

## 🔹 Key Features

- **Hospital Management**: Add and retrieve information on hospitals.
- **Department Management**: Track hospital departments and their associations.
- **Doctor Management**: Manage doctor details, including departmental and patient associations.
- **Patient Management**: Maintain patient records, including medical history and appointments.
- **Medical Record Management**: Manage and update patient medical records and test results.
- **Appointment Scheduling**: Efficiently schedule and manage appointments.

---

## 🛠️ Technologies Used

- **Programming Language**: Python
- **Database & ORM**: SQLAlchemy, SQLite
- **Date Management**: datetime module

---

## 🚀 Installation Guide

### Prerequisites
- Python 3.x installed
- Virtual environment setup (recommended)

### Project Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mitchel-ongachi/MediVerse
   cd MediVerse
   ```

2. **Set Up Virtual Environment** (optional but recommended):
   ```bash
   python -m venv env  # or your preferred virtual environment
   source env/bin/activate  # For Windows, use env\Scripts\activate
   ```

3. **Install Dependencies**:
   Install SQLAlchemy and other required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database**:
   The database (`hospital_data.db`) will be generated automatically when running the application for the first time.

5. **Seed the Database (Optional)**:
   To add sample data, run:
   ```bash
   python -m db.seed
   ```

---

## 🖥️ Usage Instructions

### Run the Application

From the root project directory, start the CLI:
```bash
python -m lib.main
```

### Available Commands

- **Hospital Management**
  - `Add Hospital` 
  - `Get Hospital`

- **Department Management**
  - `Add Department`
  - `Get Department`

- **Doctor Management**
  - `Add Doctor`
  - `Get Doctor`

- **Patient Management**
  - `Add Patient`
  - `Get Patient`

- **Medical Record Management**
  - `Add Medical Record`
  - `Get Medical Record`
  - `Add Test Result`
  - `Get Test Result`

- **Appointment Management**
  - `Schedule Appointment`
  - `Get Appointment`
  - `Exit`

### Example Commands

**Adding a Hospital**
```plaintext
Enter your choice: 1
Enter hospital name (default: St Mary): My Hospital
Enter hospital location (default: Nairobi): Nairobi
Enter contact number (default: 555-666): 555-123
```

**Retrieving a Patient**
```plaintext
Enter your choice: 6
Enter patient ID: 1
Patient ID: 1, Name: John Doe, DOB: 1990-01-01, Doctor ID: 1
```

---

## 👥 Contributing

Contributions are encouraged! To suggest improvements or new features, please submit a pull request or open an issue.

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 📚 Acknowledgments

- [SQLAlchemy](https://www.sqlalchemy.org/): ORM library for Python
- [SQLite](https://www.sqlite.org/): Lightweight relational database

