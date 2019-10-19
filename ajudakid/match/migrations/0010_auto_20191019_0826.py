# Generated by Django 2.2.6 on 2019-10-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0009_delete_acao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interesse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=130)),
            ],
        ),
        migrations.AddField(
            model_name='apoiador',
            name='interesses',
            field=models.ManyToManyField(to='match.Interesse'),
        ),
    ]