from django.contrib import admin
from .models import Answers, Sertif

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('title', 'users', 'skills', 'score', 'date')
    list_filter = ('users', 'skills', 'date')
    search_fields = ('title', 'Users__username', 'Skills__title')
    list_per_page = 20

@admin.register(Sertif)
class SertifAdmin(admin.ModelAdmin):
    list_display = ('title', 'users', 'blank', 'date')
    list_filter = ('users', 'blank', 'date')
    search_fields = ('title', 'Users__username', 'Blank__title')
    list_per_page = 20
