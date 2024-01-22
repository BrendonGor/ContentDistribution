from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subject(models.Model):
    """Academic discipline (math, physics, etc.)"""

    name = models.CharField(max_length=1000, unique=True, null=False)
    description = models.TextField()
    # Other subject fields


class Course(models.Model):
    """A Course within a subject (e.g. calculus within math)"""

    # if a subject has a course I cannot delete that course without deleting the subject.
    subject = models.ForeignKey(
        Subject, on_delete=models.PROTECT, unique=True, related_name="courses"
    )  # A course belongs to a subject, can also access using courses instead of course_set

    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(null=False)
    # Other topic fields


class Topic(models.Model):
    """A topic within a course (e.g. limits within calculus, dijkstras algorithm within algorithms)"""

    # default is if I delete a topic, deletes all mappings to courses. If delete a course, deletes all mappings to topics, but topics still exist.
    course = models.ManyToManyField(
        Course, related_name="topics"
    )  # A topic belongs to a course, can also access using topics instead of topic_set

    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(null=False)
    # Other topic fields


class ContentType(models.Model):
    """A type of resource (e.g. video, pdf, etc.)
    In future we can add more types as needed.
    We should also shows small box preview of the resource (e.g. a video thumbnail, or a pdf preview)
    """

    content_type = ["video", "pdf", "slides", "text", "audio", "other"]
    name = models.CharField(
        max_length=100, unique=True, null=False, choices=content_type
    )
    # Other type fields


class Resource(models.Model):
    """A resource (e.g. a YouTube video, a PDF, slides, etc.) for learning.
    It can be associated with a course, or topic. A link is either at the course, or topic level.
    For now you can pick many topics or 1 course.
    TLDR: I think it is fine to have one course. But we should allow multiple topics since lectures can cover multiple topics in a talk
    or slide show and might not be willing to slice it up for us.
    """

    topic = models.ManyToManyField(
        Topic, related_name="resources", blank=True
    )  # don't need to specify null since many to many uses relational table
    course = models.ForeignKey(
        Course,
        related_name="resources",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    types = models.ManyToManyField(
        ContentType, related_name="resources", blank=True
    )  # optional, can have no types

    url = models.URLField(unique=True, null=False)
    description = models.TextField(null=False)
    expert_score = models.IntegerField(
        null=True, blank=True, default=None
    )  # blank allows serializer to have no value for this field
    general_score = models.IntegerField(null=True, blank=True, default=None)
    # Other resource fields


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")

        user = self.model(
            email=email, first_name=first_name, last_name=last_name, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, first_name, last_name, **extra_fields)


class CustomUser(AbstractUser):
    """User model for authentication
    - https://testdriven.io/blog/django-custom-user-model/
    - https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#substituting-a-custom-user-model
    - https://docs.djangoproject.com/en/5.0/ref/contrib/auth/"""

    username = None
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=150, blank=False)

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
