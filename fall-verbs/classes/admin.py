from django.contrib import admin
from .models import Class
from .models import SuperClass
from .models import Component

admin.site.register(Class)
admin.site.register(SuperClass)
admin.site.register(Component)
