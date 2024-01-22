from django.contrib import admin
from .models import Subject, Course, Topic, ContentType, Resource, CustomUser

# Register your models here.
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(ContentType)
admin.site.register(Resource)
admin.site.register(CustomUser)
