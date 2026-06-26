# 🏥 SmartCare Hospital ERP System

A Hospital Management System developed using Flask, MySQL, HTML, CSS, and Python.

## 🚀 Features

* Patient Management

  * Add Patient
  * View Patient
  * Search Patient
  * Update Patient
  * Delete Patient

* Doctor Management

  * Add Doctor
  * View Doctor
  * Search Doctor
  * Update Doctor
  * Delete Doctor

* Appointment Management

  * Book Appointment
  * View Appointments
  * Update Status

* Medicine Management

  * Add Medicines
  * View Medicines
  * Update Medicines
  * Delete Medicines

* Billing Management

  * Generate Bills
  * View Bills

* Medical Reports

  * Add Reports
  * View Reports

* Feedback Management

  * Add Feedback
  * View Feedback

* Statistics Dashboard

  * Total Patients
  * Total Doctors
  * Total Appointments
  * Total Medicines
  * Total Revenue

## 🛠 Technologies Used

* Python
* Flask
* MySQL
* HTML
* CSS
* Jinja2

## ▶️ How to Run

1. Create MySQL database: `hospitaldb`
2. Run SQL tables
3. Install dependencies:

pip install flask mysql-connector-python

4. Run project:

python app.py

5. Open:

http://127.0.0.1:5000

## 🔑 Login

Username: admin

Password: admin123

## 👨‍💻 Developed By

Durga Sri Havya

my project step by step process with the databases queries:

🏥 DATABASE SETUP

⚙️ 1. Database Information
---------------------------
Database Name: hospital_db
DB Type: MySQL
ORM Used: SQLAlchemy (Flask)

🧱 2. DATABASE TABLES (FULL STRUCTURE)
--------------------------------------
👨‍⚕️ 1. USERS TABLE (Login & Role Management):

create database hospital_db;
use hospital_db;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL
);

🏥 2. PATIENTS TABLE:

CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    phone VARCHAR(15),
    address TEXT,
    created_at DATE DEFAULT CURRENT_DATE
);

👨‍⚕️ 3. DOCTORS TABLE:

CREATE TABLE doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    specialization VARCHAR(100),
    phone VARCHAR(15),
    email VARCHAR(100)
);

📅 4. APPOINTMENTS TABLE:

CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    status VARCHAR(50) DEFAULT 'Pending',
    FOREIGN KEY (patient_id) REFERENCES patients(id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(id)
);

💊 5. PRESCRIPTIONS TABLE:

CREATE TABLE prescriptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    disease VARCHAR(255),
    medicine VARCHAR(255),
    prescription_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(id)
);

💰 6. BILLING TABLE:

CREATE TABLE bills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    amount DECIMAL(10,2),
    status VARCHAR(50) DEFAULT 'Unpaid',
    bill_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(id)
);

CREATE TABLE disease_medicines
(
    id INT AUTO_INCREMENT PRIMARY KEY,

    disease VARCHAR(100),

    medicine_name VARCHAR(200)
);

CREATE TABLE medicines
(
    medicine_id INT AUTO_INCREMENT PRIMARY KEY,

    medicine_name VARCHAR(100),

    price DECIMAL(10,2),

    quantity INT
);

CREATE TABLE feedback
(
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,

    patient_name VARCHAR(100),

    comments VARCHAR(500)
);

CREATE TABLE reports
(
    report_id INT AUTO_INCREMENT PRIMARY KEY,

    patient_name VARCHAR(100),

    diagnosis VARCHAR(200),

    prescription VARCHAR(200),

    report_date DATE
);

🌱 3. DEFAULT DATA INSERTION 
-----------------------------
👤 Admin Login (DEFAULT USER):

INSERT INTO users (username, password, role)
VALUES ('admin', 'admin123', 'admin');

👨‍⚕️ Sample Doctor Data:

INSERT INTO doctors (name, specialization, phone, email)
VALUES 
('Karthik', 'Cardiologist', '9876543210', 'karthik@gmail.com'),
('Ravi', 'Neurologist', '9123456780', 'ravi@gmail.com');

🏥 Sample Patient Data:

INSERT INTO patients (name, age, gender, phone, address)
VALUES 
('Siva', 25, 'Male', '9000011111', 'Chennai'),
('Anitha', 30, 'Female', '9000022222', 'Bangalore');

📅 Sample Appointment:

INSERT INTO appointments (patient_id, doctor_id, appointment_date, status)
VALUES (1, 1, '2026-06-25', 'Confirmed');

💊 Sample Prescription:

INSERT INTO prescriptions (patient_id, doctor_id, disease, medicine, prescription_date)
VALUES (1, 1, 'Fever', 'Paracetamol', '2026-06-25');

INSERT INTO disease_medicines
(disease, medicine_name)
VALUES
('fever','Paracetamol'),
('cold','Cetirizine'),
('cough','Benadryl Syrup'),
('headache','Ibuprofen'),
('acidity','Pantoprazole'),
('diabetes','Metformin'),
('hypertension','Amlodipine'),
('asthma','Salbutamol Inhaler'),
('allergy','Levocetirizine'),
('migraine','Sumatriptan'),
('gastritis','Omeprazole'),
('vomiting','Ondansetron'),
('diarrhea','ORS + Loperamide'),
('constipation','Lactulose Syrup'),
('anemia','Ferrous Sulphate'),
('arthritis','Diclofenac'),
('back pain','Aceclofenac'),
('toothache','Ibuprofen'),
('ear infection','Amoxicillin'),
('skin infection','Mupirocin Ointment'),
('fungal infection','Clotrimazole'),
('urinary infection','Nitrofurantoin'),
('bronchitis','Azithromycin'),
('pneumonia','Amoxicillin-Clavulanate'),
('thyroid','Levothyroxine'),
('vitamin d deficiency','Vitamin D3'),
('b12 deficiency','Methylcobalamin'),
('insomnia','Melatonin'),
('dehydration','ORS'),
('heartburn','Pantoprazole');

🔄 4. HOW TO SETUP PROJECT ON NEW LAPTOP
-----------------------------------------

Step 1: Create DB

CREATE DATABASE hospital_db;

Step 2: Run all table queries above
Step 3: Insert default data
Step 4: Update Flask config

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/hospital_db'

⭐ BONUS (VERY IMPORTANT FOR YOUR ROLE-BASED SYSTEM)
-----------------------------------------------------

## 🔐 ROLE BASED ACCESS

- Admin → Full access (users, doctors, patients, billing)
- Doctor → View patients, create prescriptions
- Receptionist → Manage appointments, patients
- Pharmacist → View prescriptions only

🏥 My Project Structure
------------------------

HospitalManagementSystem/
│
├── app.py                          # Main Flask file (ALL routes + login logic here)
│
├── /templates/
│   ├── login.html                  # Login page (admin/doctor)
│   ├── admin_dashboard.html        # Admin dashboard
│   ├── doctor_dashboard.html       # Doctor dashboard
│   ├── patient_dashboard.html      # Patient dashboard
│   │
│   ├── prescription.html           # Prescription page (print issue + UI fixes)
│   ├── medicine.html               # Medicine management page
│   ├── appointment.html            # Appointment page
│   │
│   ├── error.html or login_failed.html   # Invalid login UI page (not professional yet)
│
├── /static/
│   ├── style.css                   # All UI styling (boxes, layout, buttons)
│   ├── script.js                   # Basic JS (if used)
│
├── /database/
│   ├── hospital.db                 # SQLite database file
│
├── /uploads/ (optional)
│   ├── prescriptions/              # Saved or generated files (if implemented)
│
└── README.md                       # Basic project notes (not fully structured yet)