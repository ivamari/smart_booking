from django.core.management.base import BaseCommand

from crm.services.client_generator import FakeClientGenerator


class Command(BaseCommand):
    help = 'Создать n-e количество клиентов'

    def handle(self, *args, **kwargs):
        count = int(input('Введите количество клиентов: '))
        FakeClientGenerator().generate_clients(count)
        self.stdout.write(self.style.SUCCESS(
            f'Добавлено {count} новых записей Client'))

