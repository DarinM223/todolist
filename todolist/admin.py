from django.contrib import admin
from todolist.models import TodoList, TodoField

class TodoFieldInline(admin.TabularInline):
    model = TodoField

class TodoListAdmin(admin.ModelAdmin):
    model = TodoList
    inlines = [TodoFieldInline]

# Register your models here.
admin.site.register(TodoList, TodoListAdmin)
