from django.contrib import admin

# Register your models here.

from .models import project, Review, Tag
admin.site.register(project)
admin.site.register(Review)
admin.site.register(Tag)