import smtplib, ssl

port = 465
#password = input("type your password: ")

sender_email = "{{sender}}@gmail.com"
reciever_email = "{{reciever}}@gmail.com"

message_relax = """You can take it easy and relax at home, \nyour symptoms aren't too dangerous right now. \nMake sure you moniter your symtoms."""

message_prescription = """The doctor will mail you a prescription\n for your symptoms."""

message_appointment = """I have booked an appointment for you at 5pm tomorrow\n at the nearest hospital."""

mail_prescription = """\
Subject: Prescription for patient


Please pass a prescription to the patient.
Mail id: {{doctor}}@gmail.com
Patient details and symptoms:"""

mail_appointment = """\
Subject: Appointment for patient at 5pm


The patient has an appointment with you at 5pm
Mail id: {{doctor}}@gmail.com
Patient details and symptoms:"""

#Create a secure ssl context
context = ssl.create_default_context()


def prepare_and_send_result_mail(severity, patient_data):  #Call this.
    if severity<3:
        return message_relax

    elif 3<severity<7:
        mail = mail_prescription
        mail = prepare_mail(mail, patient_data)
        send_mail(mail)
        return message_prescription

    elif severity>7:
        mail = mail_appointment
        mail = prepare_mail(mail, patient_data)
        send_mail(mail)
        return message_appointment

def prepare_mail(mail, patient_data):
    mail += "\nGender: " + patient_data[0]
    mail += "\nAge: " + str(patient_data[1])
    mail += "\nSymptoms: " + ','.join(patient_data[2])
    if not patient_data[2]:
        mail += "None"
    mail += "\nPre-existing conditions: " + ','.join(patient_data[3])
    if not patient_data[3]:
        mail += "None"
    return mail

def send_mail(mail):  #Don't call this.
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("hackathon1231@gmail.com", password)
        server.sendmail(sender_email, reciever_email, mail)
