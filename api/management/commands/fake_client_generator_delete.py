from django.core.management.base import BaseCommand

from clients.models.clients import Client


class Command(BaseCommand):
    help = 'Удалить n-e количество клиентов'

    def handle(self, *args, **kwargs):
        count = int(
            input('Введите количество клиентов для удаления: '))

        clients_to_delete = Client.objects.order_by('-id')[:count]

        clients_id = clients_to_delete.values_list('id', flat=True)

        deleted_count, details = Client.objects.filter(id__in=clients_id).delete()

        if deleted_count > 0:
            self.stdout.write(self.style.SUCCESS(
                f'Удалено {deleted_count} записей из Client'))
        else:
            self.stdout.write(self.style.WARNING('Нет записей для удаления'))

