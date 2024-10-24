
from django.contrib import admin
from .models import TodoItem

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('task', 'completed')  # Fields to display in the list view
    list_filter = ('completed',)           # Add a filter for completed tasks
    search_fields = ('task',)              # Add a search box for tasks
