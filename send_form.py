#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Import smtplib for the actual sending function
import smtplib
import cgi

# Get form data
form = cgi.FieldStorage()
email = form['email'].value
message = form['message'].value

# Import the email modules we'll need
from email.message import EmailMessage

print("Content-Type: text/html; charset=utf-8")
print("")

msg = EmailMessage()
msg.set_content("Sender is: " + email + "\n" "Message is: " + message)

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Message from Portfolio site!'
msg['From'] = 'info@justin-oreilly.com'
msg['To'] = 'joreilly25@gmail.com'

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()

print("""\
<html>
    <link
        rel="stylesheet"
        href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
        crossorigin="anonymous"
    />
    <link rel="stylesheet" href="css/form.css" />
    <head>
        <title>Thank you for your message.</title>
    </head>
    <body>
        <div class="container">
            <h1>Thank You!</h1>
            <h2>I will be in touch soon.</h2>
            <h4>If you aren't redirected <a href="index.html">Click here to go back to main site.</a></h4>
        </div>
        \
    </body>
    <script>
        setTimeout(function() {
            window.location.href = "index.html";
        }, 2000);
    </script
</html>
""")