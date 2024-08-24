from django.contrib.auth.models import Group as BaseGroup


class Group(BaseGroup):
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name
