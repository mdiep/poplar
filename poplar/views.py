
from datetime import datetime

from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson

from django.contrib.auth.decorators import login_required
from django.contrib.sites.models    import get_current_site

from poplar.models import Person, Group, Action
from poplar.forms import PersonForm, NoteForm

@login_required
def activity_feed(request):
    groups  = Group.objects.all()
    site    = get_current_site(request)
    actions = Action.objects.filter(is_public=True).exclude(actor=request.user)[:20]
    return render_to_response('poplar/activity_feed.html', locals(),
                              context_instance=RequestContext(request))

@login_required
def everyone(request):
    return person_list(request, people=Person.objects.all(), title='Everyone')

@login_required
def person(request, id):
    person = get_object_or_404(Person, id=id)
    notes  = person.notes.filter(Q(is_public=True) | Q(author=request.user))[:10]
    groups = Group.objects.all()
    site   = get_current_site(request)
    if request.POST:
        note_form = NoteForm(request.POST, author=request.user, subject=person)
    else:
        note_form = NoteForm()
    return render_to_response('poplar/person.html', locals(),
                              context_instance=RequestContext(request))

@login_required
def person_add(request):
    site    = get_current_site(request)
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            action = Action(timestamp=datetime.now(),
                            is_public=True,
                            actor=request.user,
                            verb='ad',
                            person=person)
            action.save()
            return HttpResponseRedirect(reverse('person', args=[person.id]))
    else:
        form = PersonForm()
    return render_to_response('poplar/person_add.html', locals(),
                              context_instance=RequestContext(request))

@login_required
def person_edit(request, id):
    person = get_object_or_404(Person, id=id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('person', args=[person.id]))
    else:
        form = PersonForm(instance=person)
    return render_to_response('poplar/person_edit.html', locals(),
                              context_instance=RequestContext(request))

@login_required
def person_list(request, people, title):
    groups = Group.objects.all()
    site   = get_current_site(request)
    return render_to_response('poplar/person_list.html', locals(),
                              context_instance=RequestContext(request))

@login_required
def note_add(request, person_id):
    subject = get_object_or_404(Person, id=person_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, author=request.user, subject=subject)
        if form.is_valid():
            note   = form.save()
            action = Action(timestamp=datetime.now(),
                            is_public=note.is_public,
                            actor=request.user,
                            verb='wr',
                            note=note,
                            person=subject)
            action.save()
            return HttpResponseRedirect(reverse('person', args=[subject.id]))
    return person(request, person_id)

@login_required
def group(request, slug):
    group  = get_object_or_404(Group, slug=slug)
    return person_list(request, people=group.people.all(), title=group.name)

@login_required
def search(request):
    term   = request.GET['term']
    people = Person.objects.filter(name__icontains=term)
    data   = [{ 'label': unicode(p), 'url': p.get_absolute_url() } for p in people]
    return HttpResponse(simplejson.dumps(data), mimetype='application/javascript')

