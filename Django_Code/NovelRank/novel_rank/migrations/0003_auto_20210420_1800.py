# Generated by Django 3.1.3 on 2021-04-20 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novel_rank', '0002_auto_20210416_2245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hengyanmodel',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='zonghengmodel',
            options={'ordering': ['id']},
        ),
    ]
