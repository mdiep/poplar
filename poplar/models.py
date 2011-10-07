
from django.core.exceptions import ValidationError
from django.db import models

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
