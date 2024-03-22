from django.db import models
from django.contrib.auth.models import User 
from userhandle.models import Client



# Create your models here.

class JornayaUser(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True,  )
    pissword = models.CharField(max_length=100, null=False, blank=False)


class Campaign(models.Model):
    jornaya_user = models.ForeignKey(JornayaUser, on_delete=models.PROTECT, null=True, blank=True)
    campaing_id = models.CharField(max_length=100, null=False, blank=False)
    campaign_name = models.CharField(max_length=100, null=False, blank=False)


class Leads(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    cleint = models.ForeignKey(Client, on_delete=models.PROTECT, blank=True, null=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT, null=True, blank=True)
    lead_id = models.CharField(max_length=300,unique=False, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)  
    state = models.CharField(max_length=100, null=True, blank=True)
    country  = models.CharField(max_length=100, null=True, blank=True)
    claim_type = models.CharField(max_length=100)
    ip = models.CharField(max_length=100, null=False, blank=False)
    is_mail_received = models.BooleanField(default=False)
    create_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    #active prospect trusted for url 
    trusted_form_url = models.URLField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return "{} | {} | {}".format(self.lead_id, self.user.email, self.create_datetime)
    


#https://masstorthelpnow.pythonanywhere.com/create_lead/A0001C/{uniques encoded slug }/#form

class UrlSlug(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, null=True, blank=True)
    unique_slug = models.CharField(max_length=10, null=False, blank=False)
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.unique_slug} | {self.client.name} | Expired: {self.is_expired}"
    






