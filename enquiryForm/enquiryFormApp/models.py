from django.db import models
from multiselectfield import MultiSelectField

class EnquiryData (models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()

    SKILLS_CHOICES=(
        ('Py','Python'),
        ('Dj','Django'),
        ('Fl','Flask'),
        ('RAPP','Rest API')
    )
    skills=MultiSelectField(max_length=200, choices=SKILLS_CHOICES)

    LOCATION_CHOICES=(
        ('Hyd','Hyderabad'),
        ('Bang','Banglore'),
        ('Che','Chennai'),
        ('Mum','Mumbai')
    )
    locations=MultiSelectField(max_length=100,choices=LOCATION_CHOICES)
    gender=models.CharField(max_length=20)
    date=models.DateField(max_length=100)
