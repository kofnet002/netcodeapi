from django.contrib import admin
from .models import Code, User


# Register your models here.
admin.site.register([Code, User])
