import unittest
from emailSenderRHT.src.emailsender_rht.main import EmailSender

email_from = "email sender"
sender_password = "password google app"
email_to = ["receiver"]  # one or more
email_subject = "Test"
email_message = "Lorem Ipsum John Doe"


class TestEmailSender(unittest.TestCase):
    def test_send_email(self):
        emailSender = EmailSender(email_from, sender_password, email_to, email_subject, email_message)
        # Vous pouvez ajouter des assertions pour vérifier les résultats attendus
        self.assertEqual(emailSender.email_from, email_from)


if __name__ == "__main__":
    unittest.main()
