# Generated by Django 5.0.1 on 2024-02-03 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_alter_room_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(blank=True, choices=[('deluxe', 'Deluxe'), ('double', 'Double'), ('single', 'Single'), ('kids', 'Kids')], max_length=20, null=True),
        ),
    ]
