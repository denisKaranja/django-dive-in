from django.contrib import admin

# register Pools app in the admin interface
from .models import Question
admin.site.register(Question)
