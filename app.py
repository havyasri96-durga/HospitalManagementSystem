from flask import Flask, render_template, request
import mysql.connector

print("App Started")

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="hospitaldb"
)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    cursor = db.cursor()

    query = """
    SELECT *
    FROM users
    WHERE username=%s
    AND password=%s
    """

    cursor.execute(
        query,
        (
            username,
            password
        )
    )

    user = cursor.fetchone()

    cursor.close()

    if user:
        return render_template("dashboard.html")

    else:
        return "Invalid Login"
    
@app.route("/patientservices")
def patientservices():
    return render_template(
        "patientservices.html"
    )

@app.route("/addpatient")
def addpatient():
    return render_template(
        "addpatient.html"
    )

@app.route("/savepatient", methods=["POST"])
def savepatient():

    patient_name = request.form["patient_name"]
    age = request.form["age"]
    gender = request.form["gender"]
    phone = request.form["phone"]
    disease = request.form["disease"]

    cursor = db.cursor()

    query = """
    INSERT INTO patients
    (
        patient_name,
        age,
        gender,
        phone,
        disease
    )
    VALUES(%s,%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            patient_name,
            age,
            gender,
            phone,
            disease
        )
    )

    db.commit()

    cursor.close()

    return "Patient Added Successfully"

@app.route("/patients")
def patients():

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM patients"
    )

    patients = cursor.fetchall()

    cursor.close()

    return render_template(
        "patients.html",
        patients=patients
    )
@app.route("/searchpatient")
def searchpatient():
    return render_template(
        "searchpatient.html"
    )

@app.route("/findpatientrecord", methods=["POST"])
def findpatientrecord():

    patient_id = request.form["patient_id"]

    cursor = db.cursor()

    query = """
    SELECT * FROM patients
    WHERE patient_id=%s
    """

    cursor.execute(
        query,
        (patient_id,)
    )

    patient = cursor.fetchone()

    cursor.close()

    if patient:

        return render_template(
            "patientresult.html",
            patient=patient
        )

    else:

        return "Patient Not Found"
    
@app.route("/updatepatient")
def updatepatient():
    return render_template(
        "updatepatient.html"
    )

@app.route("/updatepatientrecord", methods=["POST"])
def updatepatientrecord():

    patient_id = request.form["patient_id"]
    patient_name = request.form["patient_name"]
    phone = request.form["phone"]

    cursor = db.cursor()

    query = """
    UPDATE patients
    SET patient_name=%s,
        phone=%s
    WHERE patient_id=%s
    """

    cursor.execute(
        query,
        (
            patient_name,
            phone,
            patient_id
        )
    )

    db.commit()

    cursor.close()

    return render_template(
    "success.html"
)

@app.route("/deletepatient")
def deletepatient():
    return render_template(
        "deletepatient.html"
    )

@app.route("/deletepatientrecord", methods=["POST"])
def deletepatientrecord():

    patient_id = request.form["patient_id"]

    cursor = db.cursor()

    query = """
    DELETE FROM patients
    WHERE patient_id=%s
    """

    cursor.execute(
        query,
        (patient_id,)
    )

    db.commit()

    cursor.close()

    return "Patient Deleted Successfully"

@app.route("/doctorservices")
def doctorservices():
    return render_template(
        "doctorservices.html"
    )

@app.route("/adddoctor")
def adddoctor():
    return render_template(
        "adddoctor.html"
    )

@app.route("/savedoctor", methods=["POST"])
def savedoctor():

    doctor_name = request.form["doctor_name"]
    specialization = request.form["specialization"]
    phone = request.form["phone"]
    experience = request.form["experience"]

    cursor = db.cursor()

    query = """
    INSERT INTO doctors
    (
        doctor_name,
        specialization,
        phone,
        experience
    )
    VALUES(%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            doctor_name,
            specialization,
            phone,
            experience
        )
    )

    db.commit()

    cursor.close()

    return "Doctor Added Successfully"

@app.route("/doctors")
def doctors():

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM doctors"
    )

    doctors = cursor.fetchall()

    cursor.close()

    return render_template(
        "doctors.html",
        doctors=doctors
    )

@app.route("/searchdoctor")
def searchdoctor():
    return render_template(
        "searchdoctor.html"
    )


@app.route("/finddoctorrecord", methods=["POST"])
def finddoctorrecord():

    doctor_id = request.form["doctor_id"]

    cursor = db.cursor()

    query = """
    SELECT * FROM doctors
    WHERE doctor_id=%s
    """

    cursor.execute(
        query,
        (doctor_id,)
    )

    doctor = cursor.fetchone()

    cursor.close()

    if doctor:

        return render_template(
            "doctorresult.html",
            doctor=doctor
        )

    return "Doctor Not Found"

@app.route("/updatedoctor")
def updatedoctor():
    return render_template(
        "updatedoctor.html"
    )

@app.route("/updatedoctorrecord", methods=["POST"])
def updatedoctorrecord():

    doctor_id = request.form["doctor_id"]
    doctor_name = request.form["doctor_name"]
    phone = request.form["phone"]

    cursor = db.cursor()

    query = """
    UPDATE doctors
    SET doctor_name=%s,
        phone=%s
    WHERE doctor_id=%s
    """

    cursor.execute(
        query,
        (
            doctor_name,
            phone,
            doctor_id
        )
    )

    db.commit()

    cursor.close()

    return "Doctor Updated Successfully"

@app.route("/deletedoctor")
def deletedoctor():
    return render_template(
        "deletedoctor.html"
    )

@app.route("/deletedoctorrecord", methods=["POST"])
def deletedoctorrecord():

    doctor_id = request.form["doctor_id"]

    cursor = db.cursor()

    query = """
    DELETE FROM doctors
    WHERE doctor_id=%s
    """

    cursor.execute(
        query,
        (doctor_id,)
    )

    db.commit()

    cursor.close()

    return "Doctor Deleted Successfully"

@app.route("/appointmentservices")
def appointmentservices():
    return render_template(
        "appointmentservices.html"
    )

@app.route("/bookappointment")
def bookappointment():
    return render_template(
        "bookappointment.html"
    )

@app.route("/saveappointment", methods=["POST"])
def saveappointment():

    patient_name = request.form["patient_name"]
    doctor_name = request.form["doctor_name"]
    appointment_date = request.form["appointment_date"]

    status = "Pending"

    cursor = db.cursor()

    query = """
    INSERT INTO appointments
    (
        patient_name,
        doctor_name,
        appointment_date,
        status
    )
    VALUES(%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            patient_name,
            doctor_name,
            appointment_date,
            status
        )
    )

    db.commit()

    cursor.close()

    return "Appointment Booked Successfully"

@app.route("/appointments")
def appointments():

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM appointments"
    )

    appointments = cursor.fetchall()

    cursor.close()

    return render_template(
        "appointments.html",
        appointments=appointments
    )

@app.route("/updateappointment")
def updateappointment():
    return render_template(
        "updateappointment.html"
    )

@app.route("/updateappointmentrecord", methods=["POST"])
def updateappointmentrecord():

    appointment_id = request.form["appointment_id"]
    status = request.form["status"]

    cursor = db.cursor()

    query = """
    UPDATE appointments
    SET status=%s
    WHERE appointment_id=%s
    """

    cursor.execute(
        query,
        (
            status,
            appointment_id
        )
    )

    db.commit()

    cursor.close()

    return "Appointment Status Updated Successfully"

@app.route("/medicineservices")
def medicineservices():
    return render_template(
        "medicineservices.html"
    )

@app.route("/addmedicine")
def addmedicine():
    return render_template(
        "addmedicine.html"
    )

@app.route("/savemedicine", methods=["POST"])
def savemedicine():

    medicine_name = request.form["medicine_name"]
    price = request.form["price"]
    quantity = request.form["quantity"]

    cursor = db.cursor()

    query = """
    INSERT INTO medicines
    (
        medicine_name,
        price,
        quantity
    )
    VALUES(%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            medicine_name,
            price,
            quantity
        )
    )

    db.commit()

    cursor.close()

    return "Medicine Added Successfully"

@app.route("/medicines")
def medicines():

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM medicines"
    )

    medicines = cursor.fetchall()

    cursor.close()

    return render_template(
        "medicines.html",
        medicines=medicines
    )

@app.route("/searchmedicine")
def searchmedicine():
    return render_template(
        "searchmedicine.html"
    )


@app.route("/findmedicine", methods=["POST"])
def findmedicine():

    medicine_id = request.form["medicine_id"]

    cursor = db.cursor()

    query = """
    SELECT * FROM medicines
    WHERE medicine_id=%s
    """

    cursor.execute(
        query,
        (medicine_id,)
    )

    medicine = cursor.fetchone()

    cursor.close()

    if medicine:

        return render_template(
            "medicineresult.html",
            medicine=medicine
        )

    else:

        return "Medicine Not Found"
    
@app.route("/updatemedicine")
def updatemedicine():
    return render_template(
        "updatemedicine.html"
    )


@app.route("/updatemedicinerecord", methods=["POST"])
def updatemedicinerecord():

    medicine_id = request.form["medicine_id"]
    price = request.form["price"]
    quantity = request.form["quantity"]

    cursor = db.cursor()

    query = """
    UPDATE medicines
    SET price=%s,
        quantity=%s
    WHERE medicine_id=%s
    """

    cursor.execute(
        query,
        (
            price,
            quantity,
            medicine_id
        )
    )

    db.commit()

    cursor.close()

    return "Medicine Updated Successfully"

@app.route("/deletemedicine")
def deletemedicine():
    return render_template(
        "deletemedicine.html"
    )


@app.route("/deletemedicinerecord", methods=["POST"])
def deletemedicinerecord():

    medicine_id = request.form["medicine_id"]

    cursor = db.cursor()

    query = """
    DELETE FROM medicines
    WHERE medicine_id=%s
    """

    cursor.execute(
        query,
        (medicine_id,)
    )

    db.commit()

    cursor.close()

    return "Medicine Deleted Successfully"

@app.route("/billingservices")
def billingservices():
    return render_template(
        "billingservices.html"
    )

@app.route("/addbill")
def addbill():
    return render_template(
        "addbill.html"
    )

@app.route("/savebill", methods=["POST"])
def savebill():

    patient_name = request.form["patient_name"]
    amount = request.form["amount"]

    payment_status = "Pending"

    cursor = db.cursor()

    query = """
    INSERT INTO bills
    (
        patient_name,
        amount,
        payment_status
    )
    VALUES(%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            patient_name,
            amount,
            payment_status
        )
    )

    db.commit()

    cursor.close()

    return "Bill Generated Successfully"

@app.route("/bills")
def bills():

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM bills"
    )

    bills = cursor.fetchall()

    cursor.close()

    return render_template(
        "bills.html",
        bills=bills
    )

@app.route("/updatebill")
def updatebill():
    return render_template(
        "updatebill.html"
    )

@app.route("/updatebillrecord", methods=["POST"])
def updatebillrecord():

    bill_id = request.form["bill_id"]
    payment_status = request.form["payment_status"]

    cursor = db.cursor()

    query = """
    UPDATE bills
    SET payment_status=%s
    WHERE bill_id=%s
    """

    cursor.execute(
        query,
        (
            payment_status,
            bill_id
        )
    )

    db.commit()

    cursor.close()

    return "Payment Status Updated Successfully"

@app.route("/reportservices")
def reportservices():
    return render_template(
        "reportservices.html"
    )

@app.route("/addreport")
def addreport():
    return render_template(
        "addreport.html"
    )

@app.route("/savereport", methods=["POST"])
def savereport():

    patient_name = request.form["patient_name"]
    diagnosis = request.form["diagnosis"]
    prescription = request.form["prescription"]
    report_date = request.form["report_date"]

    cursor = db.cursor()

    query = """
    INSERT INTO reports
    (
        patient_name,
        diagnosis,
        prescription,
        report_date
    )
    VALUES(%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            patient_name,
            diagnosis,
            prescription,
            report_date
        )
    )

    db.commit()

    cursor.close()

    return "Medical Report Added Successfully"

@app.route("/reportslist")
def reportslist():

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM reports"
    )

    reports = cursor.fetchall()

    cursor.close()

    return render_template(
        "reportslist.html",
        reports=reports
    )

@app.route("/searchreport")
def searchreport():
    return render_template(
        "searchreport.html"
    )


@app.route("/findreport", methods=["POST"])
def findreport():

    report_id = request.form["report_id"]

    cursor = db.cursor()

    query = """
    SELECT *
    FROM reports
    WHERE report_id=%s
    """

    cursor.execute(
        query,
        (report_id,)
    )

    report = cursor.fetchone()

    cursor.close()

    if report:

        return render_template(
            "reportresult.html",
            report=report
        )

    else:

        return "Report Not Found"
    
@app.route("/feedbackservices")
def feedbackservices():
    return render_template(
        "feedbackservices.html"
    )

@app.route("/addfeedback")
def addfeedback():
    return render_template(
        "addfeedback.html"
    )

@app.route("/savefeedback", methods=["POST"])
def savefeedback():

    patient_name = request.form["patient_name"]
    comments = request.form["comments"]

    cursor = db.cursor()

    query = """
    INSERT INTO feedback
    (
        patient_name,
        comments
    )
    VALUES(%s,%s)
    """

    cursor.execute(
        query,
        (
            patient_name,
            comments
        )
    )

    db.commit()

    cursor.close()

    return "Feedback Added Successfully"

@app.route("/feedbacks")
def feedbacks():

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM feedback"
    )

    feedbacks = cursor.fetchall()

    cursor.close()

    return render_template(
        "feedbacks.html",
        feedbacks=feedbacks
    )

@app.route("/statistics")
def statistics():

    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM patients")
    total_patients = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM doctors")
    total_doctors = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM appointments")
    total_appointments = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM medicines")
    total_medicines = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM bills")
    total_bills = cursor.fetchone()[0]

    cursor.execute("""
    SELECT SUM(amount)
    FROM bills
    """)

    revenue = cursor.fetchone()[0]

    if revenue is None:
        revenue = 0

    cursor.close()

    return render_template(
        "statistics.html",
        total_patients=total_patients,
        total_doctors=total_doctors,
        total_appointments=total_appointments,
        total_medicines=total_medicines,
        total_bills=total_bills,
        revenue=revenue
    )

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/reports")
def reports():

    cursor = db.cursor()

    query = """
    SELECT *
    FROM reports
    """

    cursor.execute(query)

    reports = cursor.fetchall()

    cursor.close()

    return render_template(
        "reports.html",
        reports=reports
    )

@app.route("/prescription")
def prescription():
    return render_template(
        "prescription.html"
    )

if __name__ == "__main__":
    app.run(debug=True)