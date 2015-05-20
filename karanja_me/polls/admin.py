from django.contrib import admin

# register Pools app in the admin interface
from .models import Choice, Question

class ChoiceInLine(admin.StackedInline):
  model = Choice
  extra = 3


class QuestionAdmin(admin.ModelAdmin):
  # re-order which field comes first
  fieldsets = [
    ("Question",         {"fields": ["question_text"]}),
    ("Date Information", {"fields": ["pub_date"], "classes": ["collapse"]})
  ]

  inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)


