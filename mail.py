import smtplib, ssl


# A function that sends the email of the result to hadas.c@velismedia.com.


def sendemail(message):
    from_addr = 'derby50bb@gmail.com'
    password = "tonitoni12"
    receiver = 'roiyad95@gmail.com'
    final_message = """\Subject: Finished the program
     """ + message
    port = 465  # SSL port
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(from_addr, password)
        server.sendmail(from_addr, receiver, final_message)
