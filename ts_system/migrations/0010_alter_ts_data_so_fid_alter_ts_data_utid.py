# Generated by Django 4.0.4 on 2022-08-23 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts_system', '0009_alter_ts_data_so_fid_alter_ts_data_utid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ts_data',
            name='SO_FID',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='ts_data',
            name='UTID',
            field=models.CharField(max_length=250, primary_key=True, serialize=False, unique=True),
        ),
    ]
