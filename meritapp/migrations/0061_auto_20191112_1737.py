# Generated by Django 2.2.6 on 2019-11-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meritapp', '0060_auto_20191112_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='enable_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='courses',
            name='enable_trending',
            field=models.BooleanField(default=False),
        ),
    ]