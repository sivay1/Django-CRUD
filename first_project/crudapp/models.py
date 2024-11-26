from django.db import models

# Create your models here.

class Details(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    GENDER_SELECTION =[
        ("Male", "Male"),
        ("Female", "Female")
    ]
    gender = models.CharField(max_length=10, choices=GENDER_SELECTION, blank=True, null=True)