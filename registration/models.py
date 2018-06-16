from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    duty = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20)
    invite_code = models.CharField(max_length=20, null=True)

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
