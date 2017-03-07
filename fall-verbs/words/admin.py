from django.contrib import admin

from .models import Word
from .models import Sense
from .models import Example
from .models import Task




# Регистрируем все модели базы данных в панели администратора
admin.site.register(Word)
admin.site.register(Sense)
admin.site.register(Example)
admin.site.register(Task)