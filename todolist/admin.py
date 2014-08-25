from django.contrib import admin
from todolist.models import TodoList
from todofield.admin import TodoFieldInline

class TodoListAdmin(admin.ModelAdmin):
    model = TodoList
    inlines = [TodoFieldInline]

# Register your models here.
admin.site.register(TodoList, TodoListAdmin)
