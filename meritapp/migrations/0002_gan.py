# Generated by Django 2.2.6 on 2019-10-27 15:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meritapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('seconddescription', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'gan',
                'verbose_name_plural': 'gan',
                'db_table': 'gan',
            },
        ),
    ]