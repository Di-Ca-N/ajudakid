# Generated by Django 2.2.6 on 2019-10-19 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0003_auto_20191019_0332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entidade',
            name='username',
        ),
    ]
