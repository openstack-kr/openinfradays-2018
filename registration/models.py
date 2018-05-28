from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TicketType(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.name


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    pay_uuid = models.CharField(max_length=32)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.SET_NULL)
    amount = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20)
    transaction_code = models.CharField(max_length=36, blank=True)
    payment_status = models.CharField(
        max_length=10,
        default='ready',
        choices=(
            ('ready', u'Ready'),
            ('paid', u'Paid'),
            ('deleted', u'Deleted'),
            ('cancelled', u'Cancelled'),
        )
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    confirmed = models.DateTimeField(null=True, blank=True)
    canceled = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.email, self.ticket_type.name)


class ConferenceTicket(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    confirmed = models.DateTimeField(null=True, blank=True)
    canceled = models.DateTimeField(null=True, blank=True)