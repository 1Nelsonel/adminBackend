from django.db import models

# Create your models here.
class Member(models.Model):
    regId = models.CharField(max_length=10, db_index=True, null=False)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=100)