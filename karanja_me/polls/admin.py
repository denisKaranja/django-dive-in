from django.contrib import admin

# register Pools app in the admin interface
from .models import Choice, Question

class ChoiceInLine(admin.TabularInline):
  model = Choice
  extra = 3


class QuestionAdmin(admin.ModelAdmin):
  # re-order which field comes first
  fieldsets = [
    ("Question",         {"fields": ["question_text"]}),
    ("Date Information", {"fields": ["pub_date"], "classes": ["collapse"]})
  ]

  list_display = ("question_text", "pub_date", "was_published_recently")
  list_filter = ["pub_date"] # adds a filter to the sidebar
  search_fileds = ["question_text"]

  inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)


