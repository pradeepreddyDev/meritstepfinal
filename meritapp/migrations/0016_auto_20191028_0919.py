# Generated by Django 2.2.6 on 2019-10-28 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meritapp', '0015_auto_20191028_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hom',
            name='courcetitle',
        ),
        migrations.RemoveField(
            model_name='hom',
            name='image',
        ),
    ]
