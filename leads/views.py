from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings 
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, get_connection, send_mail, send_mass_mail
# from ipware import get_client_ip
import smtplib
import os 
from .models import Leads
from .utils import get_client_ip, pennsylvania_time
from .alertemails import alert_email_duplicate_leadid, alert_email_no_leadid
from .retain import retain
from userhandle.models import Client

from dotenv import load_dotenv

load_dotenv()

import requests

def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        data = response.json()
        return data['ip']
    except Exception as e:
        print("IP address was not found!")
        return None
    




def index(request):
    if request.user.is_authenticated:
        try: 
            client = Client.objects.get(user=request.user)
        except Exception:
            return HttpResponse("Client id not found!")
        
        cid = client.unique_id
        # print("unique client id : ", client_id)
        # redirect_url = f"/create_lead?client_id={client_id}"
        return redirect("create_lead", client_id=cid)
    else: 
        return redirect("client-login")



def create_lead(request, client_id):
    # client_id = request.GET.get('client_id', None)

    if client_id is None:
        return HttpResponse("Client Id missing.")
    
    if request.method == "POST":
        first_name = request.POST.get("form_fields[field_7aef3a3]", "")
        last_name = request.POST.get("form_fields[field_06c9e6b]", "")
        email = request.POST.get("form_fields[field_98d7f1c]", "")  
        phone = request.POST.get("form_fields[field_8cf97c2]", "")
        lead_id = request.POST.get("form_fields[field_179df87]", "")
        claim_type = request.POST.get("form_fields[field_ef66416]", "")
        cert_url = request.POST.get("xxTrustedFormCertUrl", "")
        leads = Leads.objects.filter(lead_id=lead_id)
        ip = get_client_ip(request)
        # print("ip : ", ip)
        if ip == None or ip == "":
            return HttpResponse("Ip address not generated")
        # print(ip)
        if lead_id == "":
            alert_email_no_leadid(client_id=client_id)
            return HttpResponse("Lead id is none!") #find a better way to display this 
        if leads.exists():
            # print("Duplicate lead id found!")
            alert_email_duplicate_leadid(leadid=lead_id, client_id=client_id)

        client = Client.objects.get(unique_id=client_id)
        client_user = client.user
        
        lead = Leads.objects.create(user=client_user, lead_id=lead_id,  first_name=first_name,phone=phone,
                                    last_name=last_name, email=email, ip=ip, claim_type=claim_type, trusted_form_url=cert_url)
        created_at = pennsylvania_time()
        retain(cert_url=cert_url, email=email)
        user_html = render_to_string('email_template.html', 
                                {'lead': lead, "created_at": created_at})
        send_mail(
            'Lead Id generation!',
            "Please review the information of the lead created!",
            settings.EMAIL_HOST_USER,
                ["kundan.k.pandey02@gmail.com",client.user.email],
            html_message=user_html,)
        lead.is_mail_received = True
        lead.save()
        return render(request, "success_lead.html")
    else: 
        return render(request, "index.html", {"client_id": client_id})
    

def testenv(request):
    debug = os.getenv("DEBUG", None)
    email = os.getenv("EMAIL_HOST", None)
    pss = os.getenv("EMAIL_HOST_PASSWORD", None)
    # print(debug, email, pss)
    return HttpResponse("testing env file variables")


