from django.db import models

class StudentData(models.Model):
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField()
    dept = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class StaffData(models.Model):
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    age = models.IntegerField()
    dept = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.name