from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    director = models.ForeignKey(Person)
    actors = models.ManyToManyField(Person, related_name='actors')
    year = models.IntegerField()

    def __str__(self):
        return self.title
