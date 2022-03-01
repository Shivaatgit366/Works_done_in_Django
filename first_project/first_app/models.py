from django.db import models

# Create your models here.


# in this file, we create models(tables)/classes for the project with field names and datatypes.
class Topic(models.Model):  # every model in django must be subclass/inherited from django.db.models.Models
    top_name = models.CharField(max_length=264, unique=True)

    # we need to have string representation of the object. so, We use special functions.
    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name  # it means return the name of the webpage.


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)  # on_delete=models.CASCADE is very important
    date = models.DateField()

    def __str__(self):
        return str(self.date)  # since it's a datetime object, cast it into a string.
