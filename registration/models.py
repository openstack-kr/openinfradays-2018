from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    team = models.CharField(max_length=100, blank=True)
    duty = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20)
    company_phone_number = models.CharField(max_length=50, blank=True)
    invite_code = models.CharField(max_length=20, null=True)
    term_agreed = models.BooleanField(default=False, blank=False, null=False)
    participant_dates = models.CharField(
        max_length=20,
        default=None,
        null=True,
        blank=True,
        choices=(
            ('day1', u'1일차'),
            ('day2', u'2일차'),
            ('both', u'양일'),
        )
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    confirmed = models.DateTimeField(auto_now=True)
    canceled = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.name, self.email)


class InviteCode(models.Model):
    code = models.CharField(max_length=10)
    registered = models.BooleanField(default=False)
    user = models.ForeignKey(Registration, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.code
