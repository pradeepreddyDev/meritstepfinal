# Generated by Django 2.2.6 on 2019-10-29 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meritapp', '0019_auto_20191029_0952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hom',
            old_name='overview4',
            new_name='stories',
        ),
    ]