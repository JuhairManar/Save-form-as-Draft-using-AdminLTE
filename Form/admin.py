from django.contrib import admin
from .models import MyModel

class MyModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'is_draft']  # Customize the fields displayed in the admin list view

admin.site.register(MyModel, MyModelAdmin)
