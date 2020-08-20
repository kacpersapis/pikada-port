from django.db import models

# Create your models here.
class Trip(models.Model):
    nazwa_imprezy = models.CharField(max_length=100, blank=False, default='')
    start_date = models.DateField(null=True, blank=False)
    finish_date = models.DateField(null=True, blank=False)
    uczestnicy = models.PositiveSmallIntegerField(blank=False, default=0)
    cena = models.IntegerField(default=0)
    instutucja = models.CharField(max_length=100, blank=False, default='')
    organizator = models.CharField(max_length=100, blank=False, default='')
    wyżywienie = models.CharField(max_length=100, blank=False, default='')
    przewoźnik = models.CharField(max_length=100, default='')
    program = models.TextField(default='')
    umowa = models.TextField(default='', choices=[('Tak', 'Tak'),('Nie', 'Nie')])
    pliki = models.FileField(upload_to='pliki', null=True, blank=True)


    def __str__(self):
        return self.nazwa_i_termin()

    def nazwa_i_termin(self):
        return "{} ({} - {})".format(self.nazwa_imprezy, self.start_date, self.finish_date)

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




