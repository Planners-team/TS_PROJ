# Generated by Django 4.0.4 on 2022-09-14 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ts_system', '0021_alter_argo_data_argo_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='argo_data',
            name='Tool_start_date',
        ),
        migrations.RemoveField(
            model_name='ts_data',
            name='Tool_start_date',
        ),
    ]