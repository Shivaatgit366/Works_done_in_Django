from django.db import models
from django.urls import reverse


# Create your models/tables here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        # in the table, name of the school will be shown
        return self.name

    # we can put the function here itself so that url gets redirected to "schooldetails" view.
    def get_absolute_url(self):
        return reverse('basic_app:schooldetails', kwargs={'pk': self.pk})


class Student(models.Model):
    name = models.CharField(max_length=256)  # name of the student
    age = models.PositiveIntegerField()  # age should be a positive integer, there is a field called "PositiveIntegerField"
    
    # Here we will mention "school" column as foreign key. Then, django automatically puts the column "school_id" in the "Student" table. 
    # It matches and puts the id when we enter the school name.
    # "related_name" is called the reverse mapping. Known as "Backward relationship".
    # Django will create the column "students_id" and maps with the school ID in the School table(above table).
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        # in the table, name of the student will be shown
        return self.name
