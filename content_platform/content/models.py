from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=1000)
    # Other subject fields

class Topic(models.Model):
    subject = models.ManyToManyField(Subject, related_name='topics')  # A topic belongs to a subject, can also access using topis instead of topic_set
    name = models.CharField(max_length=100)
    # Other topic fields

class Type(models.Model):
    name = models.CharField(max_length=100)
    # Other type fields

class Resource(models.Model):
    url = models.URLField()
    description = models.TextField()
    types = models.ManyToManyField(Type, related_name='resources')  # A resource can have multiple types, can also access using types instead of type_set
    expert_score = models.IntegerField()
    general_score = models.IntegerField()
    subject = models.ForeignKey(Subject, related_name='resources', on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ForeignKey(Topic, related_name='resources', on_delete=models.SET_NULL, null=True, blank=True)
    # Other resource fields
