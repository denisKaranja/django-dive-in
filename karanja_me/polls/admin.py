from django.contrib import admin

# register Pools app in the admin interface
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
  # re-order which field comes first
  fieldsets = [
    ("Question",               {"fields": ["question_text"]}),
    ("Date Information", {"fields": ["pub_date"]})
  ]


admin.site.register(Question, QuestionAdmin)

