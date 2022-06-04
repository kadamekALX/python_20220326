from django.db import models
from django.forms import ModelForm

# Create your models here.


class Autor(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class Ksiazka(models.Model):
    tytul = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = "__all__"
