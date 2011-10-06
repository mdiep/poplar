
from django.core.exceptions import ValidationError
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name  = models.CharField(max_length=50, blank=True)
    
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
    def clean(self):
        super(Person,self).clean()
        if not self.first_name and not self.last_name:
            raise ValidationError('People must have a first or last name')
    
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
