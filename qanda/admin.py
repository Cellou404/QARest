from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'published')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('description', 'published')