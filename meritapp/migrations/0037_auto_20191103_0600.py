# Generated by Django 2.2.6 on 2019-11-03 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meritapp', '0036_auto_20191103_0555'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coursedetail3',
            new_name='Course_events',
        ),
        migrations.AlterModelOptions(
            name='course_events',
            options={'verbose_name': 'course_events', 'verbose_name_plural': 'course_events'},
        ),
        migrations.AlterModelTable(
            name='course_events',
            table='course_events',
        ),
    ]
