# Generated by Django 5.0.1 on 2024-07-29 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_picture_ismessagesthumbnail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='picture',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='testimony',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Testimonies'},
        ),
    ]
