from operator import concat
from django.contrib import admin
#import the 'user' model:
from .models import user, contact

# Register your models here.
admin.site.register(user)
admin.site.register(contact)
