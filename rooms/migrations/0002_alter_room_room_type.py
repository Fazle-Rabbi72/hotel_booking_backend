# Generated by Django 5.1.1 on 2024-09-21 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('Single', 'Single'), ('Double', 'Double'), ('Family Suite', 'Family Suite'), ('Suite', 'Suite')], max_length=50),
        ),
    ]
