from django.db import models

# Create your models here.

class HydJobPortal(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=40)
    emp_add=models.CharField(max_length=40)
    emp_designation=models.CharField(max_length=40)


class BangaloreJobPortal(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=40)
    emp_add=models.CharField(max_length=40)
    emp_designation=models.CharField(max_length=40)

class PuneJobPortal(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=40)
    emp_add=models.CharField(max_length=40)
    emp_designation=models.CharField(max_length=40)

class ChennaiJobPortal(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=40)
    emp_add=models.CharField(max_length=40)
    emp_designation=models.CharField(max_length=40)



