# Generated by Django 5.1.1 on 2024-09-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_alter_room_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book/media/uploads/'),
        ),
    ]