# Generated by Django 4.2.15 on 2024-09-07 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dicts', '0002_alter_agetype_options'),
        ('clients', '0002_alter_client_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='clients', to='dicts.gender', verbose_name='Гендер'),
            preserve_default=False,
        ),
    ]
