import smtplib, ssl

# A function that sends the email of the result to hadas.c@velismedia.com.



def sendemail(message):
    from_addr = 'derby50bb@gmail.com'
    subject = 'Finished The Program'
    login = 'hopetoworkforyou'
    password = "tonitoni12"    # So the password won't be saved as an variable
    receiver = 'hadas.c@velismedia.com'
    port = 465  # port for SSL
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(from_addr, password)
        server.sendmail(from_addr, receiver, message)

