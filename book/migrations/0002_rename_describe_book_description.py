# Generated by Django 4.2.2 on 2023-09-19 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='describe',
            new_name='description',
        ),
    ]
