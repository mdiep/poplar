
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

# Sarah wrote a note about Matt: "He's a winner!"
#  actor=Sarah, action='wrote', note="He's a winner!", person=Matt
# Sarah added 1 person: Matt
#  actor=Sarah, action='added', person=Matt
# Sarah added 5 people to South: Matt, Kathy, Jeremy, Dave, Alyssa
#  actor=Sarah, action='added', person=Matt, group=South
#  etc.
# Sarah removed 1 person from South: Matt
#  actor=Sarah, action='removed', person=Matt, group=South
# Karl created a new group: Slides
#  actor=Karl, action='created', group=Slides
class Action(models.Model):
    VERB_CHOICES = (
        ('wr', 'wrote'),
        ('ad', 'added'),
        ('rm', 'removed'),
        ('cr', 'created'), 
    )
    timestamp = models.DateTimeField()
    is_public = models.BooleanField(default=True)
    actor     = models.ForeignKey(auth.models.User, related_name='actions')
    verb      = models.CharField(max_length=2, choices=VERB_CHOICES)
    
    # optional objects
    note      = models.ForeignKey(Note,   related_name='+', null=True)
    group     = models.ForeignKey(Group,  related_name='+', null=True)
    person    = models.ForeignKey(Person, related_name='+', null=True)
    
    def __unicode__(self):
        if self.note and self.verb == 'wr':
            return '%s wrote a note about %s' % (self.actor, self.person)
        return '%s action' % (self.get_verb_display())
    
    class Meta:
        ordering = ['-timestamp']


