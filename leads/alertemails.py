from django.template.loader import render_to_string
from django.core.mail import EmailMessage, get_connection, send_mail, send_mass_mail
from django.conf import settings
from userhandle.models import Client

def alert_email_duplicate_leadid(leadid, client_id):

    send_mail(
            'Duplicate lead id created!{}'.format(leadid),
            "Please review the information of the lead created!",
            settings.EMAIL_HOST_USER,
            ["kundan.k.pandey02@gmail.com",],
            )
    

def alert_email_no_leadid(client_id):
    client = Client.objects.get(unique_id=client_id)
    send_mail(
            '{}! No lead id generated for client : !{}'.format(client.user.email, client_id),
            f"{client.user.email}! No lead generated",
            settings.EMAIL_HOST_USER,
            ["kundan.k.pandey02@gmail.com",],
            )