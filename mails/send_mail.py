import smtplib

HOST = "smtp.gmail.com"
from_email = "janedoe@gmail.com"
to_email = "rose@yahoo.com"

with smtplib.SMTP(host=HOST) as connection:
    # Engage transport layer security mode
    connection.starttls()
    connection.login(user=from_email, password="1234")
    connection.sendmail(
        from_addr=from_email,
        to_addrs=to_email,
        msg="Subject: The Great Heading\n\nBody goes here",
    )
