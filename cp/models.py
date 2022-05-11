from django.db import models

# Create your models here.
class user(models.Model):
    dbfname = models.CharField(max_length=50)
    dblname = models.CharField(max_length=50)
    dbemail = models.CharField(max_length=100)
    dbpassword = models.CharField(max_length=100)

    def __str__(self):
        return self.dbfname + " " + self.dblname
class contact(models.Model):
    dbname = models.CharField(max_length=50)
    dbemail = models.CharField(max_length=100)
    dbsubject = models.CharField(max_length=50)
    dbmessage = models.CharField(max_length=500)

    def __str__(self):
        return self.dbname + " " + self.dbsubject
