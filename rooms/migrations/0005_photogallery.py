# Generated by Django 5.1.1 on 2025-03-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_alter_room_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery/media/uploads/')),
            ],
        ),
    ]
