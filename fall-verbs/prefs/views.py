from django.shortcuts import render
from .models import Pref
from words.models import Word

def index(request):

    context = {}
    context['prefs'] = Pref.objects.all()

    return render(request, 'prefs/index.html', context)


def wordlist(request, pref_id='1'):

    context = {}

    pref = Pref.objects.get(id=pref_id)
    if pref:
        context['pref'] = pref
        context['wordlist'] = Word.objects.filter(pref=pref.id)

    return render(request, 'prefs/wordlist.html', context)