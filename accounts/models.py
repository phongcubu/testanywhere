from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create models User  login
class Customer(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    phone_field = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.user.username
