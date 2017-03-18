from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

import json

from words.models import Word
from words.models import Sense
from words.models import Example
from words.models import Task
from prefs.models import Pref
from classes.models import Class
from classes.models import Component


@csrf_exempt
def index(request):
    query = request.POST['query']
    context = {'results':[]}
    
    if query:
        query = query.lower()

        words = Word.objects.all()
        prefs = Pref.objects.all()
        classes = Class.objects.all()
        senses = Sense.objects.all()
        examples = Example.objects.all()
        tasks = Task.objects.all()

        for word in words:
            if query in word.word.lower():
                context['results'].append('Слово: %s  <a href="/words/%d/classes/">значение</a> <a href="/words/%d/tasks/">задания</a>' % (word.word, word.id, word.id))

        for pref in prefs:
            if query in pref.pref.lower():
                context['results'].append('Приставка: <a href="/prefs/%d/wordlist/">%s</a>' % (pref.id, pref.pref))

        for _class in classes:
            if query in _class.class_name:
                context['results'].append('Класс: <a href="/classes/%d/wordlist/">%s</a>' % (_class.id, _class.class_name))

        for sense in senses:
            if query in sense.sense.lower():
                context['results'].append('Значение: <a href="/words/%d/classes/">%s</a>' % (sense.id, sense.sense))

        for example in examples:
            if query in example.example.lower():
                context['results'].append('Пример: <a href="/words/%d/classes/">%s</a>' % (example.id, example.example))

        for task in tasks:
            if query in task.task.lower():
                context['results'].append('Задание: %s' % (task.task))

        return render(request, 'search/index.html', context)
    else:
        return render(request, 'search/index.html', {})


def filter_components(request):
    context = {}
    context['components'] = Component.objects.all()

    return render(request, 'search/components.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def query(request):
    data = json.loads(request.body.decode('utf-8'))

    components = Component.objects.filter(component__in=data['components'])
    classes = Class.objects.filter(components=components)
    for component in components:
        classes = classes.filter(components=component)

    result = {'classes': []}

    for cl in classes:
        result['classes'].append({
            'id': cl.id,
            'class_name': cl.class_name
        })

    return JsonResponse(result)
