from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.template.defaultfilters import date as _date
from uuid import uuid4


class AuthToken(models.Model):
    token = models.CharField(max_length=64)
    email = models.EmailField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.token = str(uuid4())
        super(AuthToken, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)


class Speaker(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100, db_index=True)
    organization = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=255, db_index=True,
                              null=True, blank=True)
    image = models.ImageField(upload_to='speaker', null=True, blank=True)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProgramCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProgramDate(models.Model):
    day = models.DateField()

    def __str__(self):
        return _date(self.day, "Y-m-d (D)")


class ProgramTime(models.Model):
    name = models.CharField(max_length=100)
    begin = models.TimeField()
    end = models.TimeField()
    day = models.ForeignKey(ProgramDate, null=True, blank=True,
                            on_delete=True)

    def __meta__(self):
        ordering = ['begin']

    def __str__(self):
        return '%s - %s (%s)' % (self.begin, self.end, self.day)


class Program(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    brief = models.TextField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    slide_url = models.CharField(max_length=255, null=True, blank=True)
    video_url = models.CharField(max_length=255, null=True, blank=True)

    date = models.ForeignKey(ProgramDate, null=True, blank=True,
                             on_delete=True)
    room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)
    times = models.ManyToManyField(ProgramTime, blank=True)
    category = models.ForeignKey(ProgramCategory, null=True, blank=True,
                                 on_delete=True)
    speaker = models.ForeignKey(Speaker, null=True, on_delete=False)

    def get_url(self):
        return reverse('program', args=[self.id])

    def get_times(self):
        times = self.times.all()

        if times:
            return '%s - %s' % (times[0].begin.strftime("%H:%M"),
                                times[len(times) - 1].end.strftime("%H:%M"))
        else:
            return "Not arranged yet"


class SponsorLevelManager(models.Manager):
    def get_queryset(self):
        return super(SponsorLevelManager, self).get_queryset()\
            .all().order_by('order')


class SponsorLevel(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    order = models.IntegerField(default=1)

    objects = SponsorLevelManager()

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='sponsor', null=True, blank=True)
    url = models.CharField(max_length=1024, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    level = models.ForeignKey(SponsorLevel, null=True, blank=True,
                              on_delete=models.SET_NULL)

    class Meta:
        ordering = ['id']

    def get_url(self):
        return reverse('sponsor', args=[self.id])

    def __str__(self):
        return self.name
