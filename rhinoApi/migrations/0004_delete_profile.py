# Generated by Django 4.1.4 on 2022-12-23 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhinoApi', '0003_remove_profile_adress_remove_profile_phone_number_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
