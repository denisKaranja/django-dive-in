from django.contrib import admin

# register Pools app in the admin interface
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
  # re-order which field comes first
  fields = ["question_text", "pub_date"]


admin.site.register(Question, QuestionAdmin)

