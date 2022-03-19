from django.db import models

# Create your models/tables here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        # in the table, name of the school will be shown
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=256)  # name of the student
    age = models.PositiveIntegerField()  # age should be a positive integer, there is a field called "PositiveIntegerField"
    
    # in the field "school", we will have school object from the Foreign Table.
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        # in the table, name of the student will be shown
        return self.name
