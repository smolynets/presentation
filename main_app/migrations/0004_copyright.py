# Generated by Django 2.2 on 2019-06-16 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_subheadertext'),
    ]

    operations = [
        migrations.CreateModel(
            name='CopyRight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='CopyRight', max_length=255)),
            ],
            options={
                'verbose_name': 'CopyRight',
            },
        ),
    ]
