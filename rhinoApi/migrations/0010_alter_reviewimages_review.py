# Generated by Django 4.1.4 on 2023-01-11 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rhinoApi', '0009_remove_review_images_reviewimages_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewimages',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='rhinoApi.review'),
        ),
    ]
