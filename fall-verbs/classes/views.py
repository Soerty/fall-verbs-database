from django.shortcuts import render
from .models import Class
from words.models import Word

def index(request):

    context = {}
    context['classes'] = Class.objects.all()

    return render(request, 'classes/index.html', context)


def wordlist(request, class_id='1'):

    context = {}

    class_obj = Class.objects.get(id=class_id)
    if class_obj:
        context['class'] = class_obj
        context['wordlist'] = Word.objects.filter(class_name=class_obj.id)

    return render(request, 'classes/wordlist.html', context)
