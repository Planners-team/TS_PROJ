# Generated by Django 4.0.4 on 2022-09-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts_system', '0032_alter_ts_data_tool_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ts_data',
            name='Open_Date',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
