
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.contrib.sites.models import get_current_site

from poplar.models import Person, Group

def activity_feed(request):
    groups = Group.objects.all()
    site   = get_current_site(request)
    return render_to_response('poplar/activity_feed.html', locals(),
                              context_instance=RequestContext(request))

def everyone(request):
    return person_list(request, people=Person.objects.all(), title='Everyone')

def person(request, id):
    person = get_object_or_404(Person, id=id)
    groups = Group.objects.all()
    site   = get_current_site(request)
    return render_to_response('poplar/person.html', locals(),
                              context_instance=RequestContext(request))

def person_list(request, people, title):
    groups = Group.objects.all()
    site   = get_current_site(request)
    return render_to_response('poplar/person_list.html', locals(),
                              context_instance=RequestContext(request))

def group(request, slug):
    group  = get_object_or_404(Group, slug=slug)
    return person_list(request, people=group.people.all(), title=group.name)
