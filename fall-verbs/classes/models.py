from django.db import models


class SuperClass(models.Model):
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name


class Component(models.Model):
    """Модель описывающая компонент"""
    component = models.CharField(max_length=50)

    def __str__(self):
        return self.component


class Class(models.Model):
    """Модель описывающая приставку"""
    superclass = models.ForeignKey(SuperClass, on_delete=models.CASCADE, blank=True, null=True)
    class_name = models.CharField(max_length=100)
    components = models.ManyToManyField(Component)
    types_choices = (
        ('физическое', 'физическое'),
        ('метафорическое', 'метафорическое')
    )
    class_type = models.CharField(max_length=30, choices=types_choices, blank=True, null=True)

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name_plural = "classes"
