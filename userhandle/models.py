from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    company_name = models.CharField(max_length=100, null=True, blank=True)
    unique_id = models.CharField(max_length=100, unique=True, blank=False, null=False)
    #standard
    cap_limit  = models.IntegerField(default=600)
    monthly_payment = models.IntegerField(default=200)
    address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} | {self.city}"
    






