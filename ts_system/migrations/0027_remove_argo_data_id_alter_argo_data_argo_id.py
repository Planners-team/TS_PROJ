# Generated by Django 4.0.4 on 2022-09-14 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts_system', '0026_ts_data_voucher_alter_ts_data_open_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='argo_data',
            name='id',
        ),
        migrations.AlterField(
            model_name='argo_data',
            name='Argo_ID',
            field=models.CharField(default=None, max_length=250, primary_key=True, serialize=False),
        ),
    ]