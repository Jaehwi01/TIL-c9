from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('menu_title',)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)