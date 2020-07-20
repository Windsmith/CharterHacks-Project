import smtplib, ssl

port = 465
#password = input("type your password: ")

sender_email = "hackathon1231@gmail.com"
reciever_email = "anandkrishna2312@gmail.com"

message_relax = """You can take it easy and relax at home, your symptoms aren't too dangerous right now. Make sure you moniter your symtoms."""

message_prescription = """The doctor will mail you a prescription for your symptoms."""

message_appointment = """I have booked an appointment for you at 5pm tomorrow at the nearest hospital."""

mail_prescription = """\
Subject: Prescription for patient


Please pass a prescription to the patient.
Mail id: rishikumarikuf@gmail.com
Patient details and symptoms:\n"""

mail_appointment = """\
Subject: Appointment for patient at 5pm


The patient has an appointment with you at 5pm
Mail id: rishikumarikuf@gmail.com
Patient details and symptoms:\n"""

#Create a secure ssl context
context = ssl.create_default_context()


def prepare_and_send_result_mail(severity, patient_data):  #Call this.
    if severity<3:
        return message_relax

    elif 3<severity<7:
        mail = mail_prescription
        for i in patient_data:
            mail += i +'\n'
        #send_mail(mail)
        return message_prescription
        
    elif severity>7:
        mail = mail_appointment
        for i in patient_data:
            mail += i +'\n'
        #send_mail(mail)
        return message_appointment

def send_mail(mail):  #Don't call this.
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("hackathon1231@gmail.com", password)
        server.sendmail(sender_email, reciever_email, mail)
