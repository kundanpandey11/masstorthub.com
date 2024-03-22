from django.http import HttpResponse
import pytz
from datetime import datetime


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def pennsylvania_time():
    et = pytz.timezone('US/Eastern')
    # Get the current time in ET
    current_time_et = datetime.now(et)
    # Format the current time as a string
    current_time_str = current_time_et.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    # print('Current Eastern Time (Pennsylvania):', current_time_str)
    return current_time_et

