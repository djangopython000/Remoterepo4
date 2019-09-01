from django import forms
from multiselectfield import MultiSelectFormField

class EnquiryForm(forms.Form):
    name=forms.CharField(
        label="enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    email=forms.EmailField(
        label="enter your email id",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'your email id'
            }
        )
    )
    mobile=forms.IntegerField(
        label="enter your mobile no",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your number'
            }
        )
    )
    SKILLS_CHOICES = (
        ('Py', 'Python'),
        ('Dj', 'Django'),
        ('Fl', 'Flask'),
        ('RAPP', 'Rest API')
    )
    skills = MultiSelectFormField(max_length=200, choices=SKILLS_CHOICES, label="select your skills")

    LOCATION_CHOICES = (
        ('Hyd', 'Hyderabad'),
        ('Bang', 'Banglore'),
        ('Che', 'Chennai'),
        ('Mum', 'Mumbai')
    )
    locations=MultiSelectFormField(max_length=200,choices=LOCATION_CHOICES,label="select your required location")

    GENDER_CHOICES=(
        ('M',"Male"),
        ('F',"Female")
    )
    gender=forms.ChoiceField(
        label="select your gender",
        widget=forms.RadioSelect(),choices=GENDER_CHOICES
    )
    y=range(1980,2020)
    date=forms.DateField(
        label="select your date",
        widget=forms.SelectDateWidget(years=y)
    )