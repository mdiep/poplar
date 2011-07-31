
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.sites.models import get_current_site

from poplar.models import Person

def activity_feed(request):
    site = get_current_site(request)
    return render_to_response('poplar/activity_feed.html', locals(),
                              context_instance=RequestContext(request))

def everyone(request):
    site   = get_current_site(request)
    people = Person.objects.all()
    return render_to_response('poplar/everyone.html', locals(),
                              context_instance=RequestContext(request))
