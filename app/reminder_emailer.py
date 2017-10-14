"""Email function for reminder app."""
import smtplib
import sys

def open_email_connection(smtp_host, smtp_port, smtp_user, smtp_pw):
    """Open an email server connection."""
    try:
        server = smtplib.SMTP_SSL(smtp_host, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(smtp_user, smtp_pw)
    except:
        print "Cannot open connection to email server."
        exit(1)

    return server

def close_email_connection(email_server):
    "Close an email server connection."""
    test_email_connection(email_server) 
    email_server.quit()

def send_email(email_server, email_sender, email_recipient, email_message):
    """Send a message and close the connection to clean up."""
    test_email_connection(email_server)
    email_server.sendmail(email_sender, email_recipient, email_message)
    
    close_email_connection(email_server)

def test_email_connection(email_server):
    "Verify an object containing an email server exists."
    try:
        email_server.ehlo()
    except:
        print "No email server connection. Exiting."
        sys.exit(1)
