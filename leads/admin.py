from django.contrib import admin
from .models import Leads, Campaign, JornayaUser, UrlSlug
# Register your models here.

admin.site.register(Leads)
admin.site.register(Campaign)
admin.site.register(JornayaUser)
admin.site.register(UrlSlug)
