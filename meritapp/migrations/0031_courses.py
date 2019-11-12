# Generated by Django 2.2.6 on 2019-11-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meritapp', '0030_auto_20191102_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('coursefee', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'courses',
                'verbose_name_plural': 'courses',
                'db_table': 'courses',
            },
        ),
    ]