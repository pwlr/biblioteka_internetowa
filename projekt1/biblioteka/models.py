from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.timezone import now

class Book(models.Model):
    WYBOR_OKLADKI = [
        ('miękka', 'miękka'),
        ('twarda', 'twarda'),
    ]
    OPCJE_PUBLIKACJI = [
        ('opublikuj', 'opublikuj'),
        ('nie publikuj', 'nie publikujh'),
    ]
    tytul = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    okladka = models.CharField(max_length=6, choices=WYBOR_OKLADKI, default='miękka')
    wydawnictwo = models.CharField(max_length=50)
    data_premiery = models.DateField(default=now, blank=True)
    data_publikacji = models.DateField(default=now, blank=True)
    liczba_stron = models.IntegerField(default=1)
    stworzono_przez = models.CharField(max_length=100, default=None, blank=True)
    zdjecie = models.ImageField(upload_to='media', default='book.jpg')
    delete = models.BooleanField(default=None, blank=True)

    def __str__(self):
        return self.tytul

    objects = models.Manager()
