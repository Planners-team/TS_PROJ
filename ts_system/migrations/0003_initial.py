# Generated by Django 4.0.4 on 2022-08-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ts_system', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ts_system',
            fields=[
                ('UTID', models.AutoField(primary_key=True, serialize=False)),
                ('Tool', models.CharField(blank=True, max_length=250)),
                ('SO_FID', models.CharField(blank=True, max_length=250)),
                ('Customer', models.CharField(blank=True, max_length=100000)),
                ('tool_status', models.CharField(blank=True, max_length=250)),
                ('Open_Date', models.CharField(blank=True, max_length=250)),
                ('Ship_Date', models.CharField(blank=True, max_length=250)),
                ('Comment', models.CharField(blank=True, max_length=250)),
                ('Handler', models.CharField(blank=True, max_length=250)),
                ('K_MAT', models.CharField(blank=True, max_length=250)),
                ('WO1', models.CharField(blank=True, max_length=250)),
                ('Tester', models.CharField(blank=True, max_length=250)),
                ('Type', models.CharField(blank=True, max_length=250)),
                ('WO2', models.CharField(blank=True, max_length=250)),
                ('BBSE', models.CharField(blank=True, max_length=250)),
                ('WO3', models.CharField(blank=True, max_length=250)),
                ('WLR_FD', models.CharField(blank=True, max_length=250)),
                ('WO4', models.CharField(blank=True, max_length=250)),
                ('OPTION_LDSR', models.CharField(blank=True, max_length=250)),
                ('WO5', models.CharField(blank=True, max_length=250)),
                ('UVR_eUVR', models.CharField(blank=True, max_length=250)),
                ('WO6', models.CharField(blank=True, max_length=250)),
                ('AiD_SSiD', models.CharField(blank=True, max_length=250)),
                ('WO7', models.CharField(blank=True, max_length=250)),
                ('Compensator', models.CharField(blank=True, max_length=250)),
                ('WO8', models.CharField(blank=True, max_length=250)),
                ('MSWAVECAL', models.CharField(blank=True, max_length=250)),
                ('WO9', models.CharField(blank=True, max_length=250)),
                ('NLR_Ceramic_Chuck', models.CharField(blank=True, max_length=250)),
                ('WO10', models.CharField(blank=True, max_length=250)),
                ('Others', models.CharField(blank=True, max_length=250)),
                ('Is_SHIPPED', models.BinaryField(default=False)),
            ],
        ),
    ]
