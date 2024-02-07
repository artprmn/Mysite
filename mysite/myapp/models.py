# myapp/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    birth_date = models.DateField()
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])

    # Другие поля и методы, если необходимо


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Добавьте другие поля по необходимости



class Campaign(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class House(models.Model):
    campaign = models.ForeignKey(Campaign, related_name='houses', on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    entrances = models.IntegerField()
    apartments_per_entrance = models.IntegerField()

    def __str__(self):
        return f"{self.city}, {self.street}, {self.house_number}"


class ApartmentVisit(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    apartment_number = models.IntegerField()
    door_opened = models.BooleanField()
    date = models.DateField()
    time = models.TimeField()
    reaction = models.CharField(max_length=20)
    contact_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=20)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Apartment(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    number = models.IntegerField()