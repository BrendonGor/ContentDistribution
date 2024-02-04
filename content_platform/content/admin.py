from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Subject, Course, Topic, ContentType, Resource, CustomUser

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(ContentType)
admin.site.register(Resource)
admin.site.register(CustomUser)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "first_name",
        "last_name",
        "is_staff",
    ]
