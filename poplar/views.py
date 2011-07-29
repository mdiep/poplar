
from django.shortcuts import render_to_response

def activity_feed(request):
    return render_to_response('poplar/activity_feed.html')
