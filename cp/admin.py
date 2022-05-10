from django.contrib import admin
#import the 'user' model:
from .models import user

# Register your models here.
admin.site.register(user)
