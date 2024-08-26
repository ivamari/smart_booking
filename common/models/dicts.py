from django.db import models


class BaseDictModelMixin(models.Model):
    code = models.CharField('Код', max_length=16, primary_key=True)
    name = models.CharField('Название', max_length=64)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.code} ({self.name})'
