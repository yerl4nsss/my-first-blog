# Generated by Django 2.2.2 on 2019-06-20 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190620_1446'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пости', 'verbose_name_plural': 'Пост'},
        ),
    ]
