# Generated by Django 4.0.4 on 2022-09-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts_system', '0031_alter_ts_data_ship_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ts_data',
            name='Tool_start_date',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]