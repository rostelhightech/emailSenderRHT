# installation
``` pip install emailsender_rht ``` 
# Using the EmailSender Class

The `EmailSender` class from the `emailsender_rht.main` package allows you to send emails using the specified information. Here's how you can use it:

1. Import the `EmailSender` class from the `emailsender_rht.main` package:

```python

/*****************************************************

from emailsender_rht.main import EmailSender

email_sender = EmailSender(
    email_from="sender@example.com",
    sender_password="your_password",
    email_to=["recipient@example.com"],
    email_subject="Email subject",
    email_message="Email message body"
)

email_sender.sendEmail()

/**************************************************************************************/

email_from: The sender's email address.
sender_password: The sender's password.
email_to`**: A list of recipient email addresses.
email_subject`**: The subject of the email.
email_message`**: The body of the email message.

