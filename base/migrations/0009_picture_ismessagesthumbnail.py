# Generated by Django 5.0.1 on 2024-07-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_event_image2_remove_event_image3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='isMessagesThumbnail',
            field=models.BooleanField(default=False),
        ),
    ]
