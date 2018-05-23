from django.db import models
from django.template.defaultfilters import date as _date


class Speaker(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100, db_index=True)
    organization = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=255, db_index=True,
                              null=True, blank=True)
    image = models.ImageField(upload_to='speaker', null=True, blank=True)
    desc = models.TextField(null=True, blank=True)


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
    rooms = models.ManyToManyField(Room, blank=True)
    times = models.ManyToManyField(ProgramTime, blank=True)
    category = models.ForeignKey(ProgramCategory, null=True, blank=True,
                                 on_delete=True)
