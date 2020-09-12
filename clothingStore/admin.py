from django.contrib import admin
from .models import Clothing, Contact,RegistrationData

# Register your models here.
admin.site.register(Clothing)
admin.site.register(Contact)
admin.site.register(RegistrationData)