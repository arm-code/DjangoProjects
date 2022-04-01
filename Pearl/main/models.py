from django.db import models

# Create your models here.
GENDER_OPTIONS = (
    ('MALE', 'MASCULINO'),
    ('female', 'FEMENINO'),
    ('other', 'OTROS')
)


class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(choices=GENDER_OPTIONS, max_length=20)
    date_birth = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class ModelsPearl(models.Model):
    name_model = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    date_certified = models.DateTimeField(auto_now=True)

class PatternsDies(models.Model):
    num_part = models.CharField(max_length=15)
    model =  models.CharField(max_length=100)
    set = models.CharField(max_length=100)

