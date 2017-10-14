"""Script to send annoying email reminders until they are completed"""
from os import environ
import sys

from reminder_emailer import open_email_connection, send_email

SMTP_HOST=environ.get('REMINDER_SMTP_HOST', 'smtp.gmail.com')
SMTP_PORT=environ.get('REMINDER_SMTP_PORT', 587)
SMTP_USER=environ.get('REMINDER_SMTP_USER', None)
SMTP_PASSWORD=environ.get('REMINDER_SMTP_PASSWORD', None)
REMINDER_DEST=environ.get('REMINDER_DESTINATION_ADDR', None)

def main():
    """Main entry point for app."""
    send_reminder()
    exit

def check_for_reminders():
    """Query DB for any reminders, pop onto stack for email."""
    pass

def close_reminders():
    """Query for any reminders that can be closed, mark as complete in DB."""
    pass

def send_reminder():
    """If reminder exists, send email."""
    msg = "THIS IS A TEST MESSAGE FROM REMINDER APP"
    email_server = open_email_connection(SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)
    send_email(email_server, SMTP_USER, REMINDER_DEST, msg) 

if __name__ == '__main__':
    sys.exit(main())
