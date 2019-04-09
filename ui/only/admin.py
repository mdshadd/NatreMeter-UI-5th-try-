from django.contrib import admin
from .models import sign
from .models import Reading

# Register your models here.

admin.site.register(sign)

admin.site.register(Reading)
