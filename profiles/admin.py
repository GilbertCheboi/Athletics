from django.contrib import admin

from .models import Profile, Academics, Training


admin.site.register(Training)
admin.site.register(Academics)
admin.site.register(Profile)