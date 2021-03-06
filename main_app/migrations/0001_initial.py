# Generated by Django 2.2 on 2019-05-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('text', models.TextField(blank=True)),
                ('is_slider', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Frame',
                'verbose_name_plural': 'Frames',
            },
        ),
        migrations.CreateModel(
            name='PageOfSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'PageOfSlider',
                'verbose_name_plural': 'PageOfSliders',
            },
        ),
    ]
