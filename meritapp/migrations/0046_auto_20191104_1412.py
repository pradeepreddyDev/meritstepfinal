# Generated by Django 2.2.6 on 2019-11-04 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meritapp', '0045_auto_20191104_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientimages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'clientimages',
                'verbose_name_plural': 'clientimages',
                'db_table': 'clientimages',
            },
        ),
        migrations.DeleteModel(
            name='Hom2',
        ),
    ]
