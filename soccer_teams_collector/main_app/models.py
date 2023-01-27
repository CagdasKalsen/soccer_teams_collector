from django.db import models

# Create your models here.


class Teams(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=250)
    country = models.CharField(max_length=50)
    stadium = models.CharField(max_length=50)
    honors = models.TextField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
