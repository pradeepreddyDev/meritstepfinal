# Generated by Django 2.2.6 on 2019-10-28 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meritapp', '0013_home'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Home',
            new_name='Hom',
        ),
        migrations.AlterModelOptions(
            name='hom',
            options={'verbose_name': 'hom', 'verbose_name_plural': 'hom'},
        ),
        migrations.AlterModelTable(
            name='hom',
            table='hom',
        ),
    ]