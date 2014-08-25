from django.contrib import admin
from todofield.models import TodoField

# Register your models here.
class TodoFieldInline(admin.TabularInline):
    model = TodoField
