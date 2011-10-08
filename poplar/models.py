
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib import auth

class Person(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'people'
    
    @models.permalink
    def get_absolute_url(self):
        return ('person', [self.id])

class Group(models.Model):
    name   = models.CharField(max_length=30, unique=True)
    slug   = models.SlugField(max_length=30, unique=True)
    people = models.ManyToManyField(Person, related_name='groups', blank=True)
    
    def __unicode__(self):
        return self.name

class Note(models.Model):
    author    = models.ForeignKey(auth.models.User, related_name='notes')
    subject   = models.ForeignKey(Person, related_name='notes')
    timestamp = models.DateTimeField()
    is_public = models.BooleanField(default=False)
    body      = models.TextField()
    
    def __unicode__(self):
        return '%s (%s on %s)' % (self.subject, self.author, self.timestamp)
    
    class Meta:
        ordering = ["-timestamp"]

