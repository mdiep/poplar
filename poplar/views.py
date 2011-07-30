
from django.shortcuts import render_to_response

from django.contrib.sites.models import get_current_site

def activity_feed(request):
    site = get_current_site(request)
    return render_to_response('poplar/activity_feed.html', locals())
