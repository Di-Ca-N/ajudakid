# Generated by Django 2.2.6 on 2019-10-19 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0005_auto_20191019_0615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acaoapoiador',
            old_name='apoiadores',
            new_name='apoiador',
        ),
    ]