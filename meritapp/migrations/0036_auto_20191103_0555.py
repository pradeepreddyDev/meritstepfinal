# Generated by Django 2.2.6 on 2019-11-03 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meritapp', '0035_auto_20191103_0523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coursedetail3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'coursedetail3',
                'verbose_name_plural': 'coursedetail3',
                'db_table': 'coursedetail3',
            },
        ),
        migrations.AddField(
            model_name='coursedetail',
            name='title7',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
