from random import Random
from django.core.mail import send_mail
from users.models import EmailVerifyRecord
from Blog.settings import EMAIL_FROM

# Generate a random string
def generate_random_string(randomlength=6):
    str = ''
    chars = '0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str = str+chars[random.randint(0, length)]
    return str

# Send Email
def register_send_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        code = generate_random_string(4)
    else:
        code = generate_random_string(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "Register link"
        email_body = "Please click the link to active your account: http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_title = "Email verification code"
        email_body = "The verification code is: {0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "Password reset link"
        email_body = "Please click the link to reset your password: http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass







