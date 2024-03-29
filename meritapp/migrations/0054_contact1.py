# Generated by Django 2.2.6 on 2019-11-07 02:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meritapp', '0053_touch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('message', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'contact1',
                'verbose_name_plural': 'contact1',
                'db_table': 'contact1',
            },
        ),
    ]
