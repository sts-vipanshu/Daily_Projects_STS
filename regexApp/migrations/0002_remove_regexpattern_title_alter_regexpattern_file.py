# Generated by Django 5.1.1 on 2024-09-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regexApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regexpattern',
            name='title',
        ),
        migrations.AlterField(
            model_name='regexpattern',
            name='file',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='temporaryFiles/'),
        ),
    ]
