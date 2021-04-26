from django.contrib import admin
from .models import ContactInfo, HelloSection, AboutSection

# Register your models here.
admin.site.register(ContactInfo)
admin.site.register(HelloSection)
admin.site.register(AboutSection)