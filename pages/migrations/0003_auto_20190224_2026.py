# Generated by Django 2.1.7 on 2019-02-24 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_contact_username_add'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Member',
        ),
    ]
