from django.db import models
from datetime import datetime
# Create your models here.
from django.contrib.auth.models import AbstractUser


class BlogUser(AbstractUser):
    usersname = models.CharField('Name', max_length=20, default='')


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="Authenting Code")
    email = models.EmailField(max_length=50, verbose_name="email")
    send_type = models.CharField(verbose_name="Type of Authentication", choices=(("register", "registe"), ("forget", "Find your password"), ("update_email","Update email")), max_length=30)
    send_time = models.DateTimeField(verbose_name="Send Time", default=datetime.now)

    class Meta:
        verbose_name = "Email Authenticating Code"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)