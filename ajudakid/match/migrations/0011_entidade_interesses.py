# Generated by Django 2.2.6 on 2019-10-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0010_auto_20191019_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='entidade',
            name='interesses',
            field=models.ManyToManyField(to='match.Interesse'),
        ),
    ]
