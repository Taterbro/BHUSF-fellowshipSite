# Generated by Django 5.0.1 on 2024-07-16 20:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_event_slug_testimony_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='testimony',
            name='testimony',
            field=ckeditor.fields.RichTextField(),
        ),
    ]