# Generated by Django 5.0.3 on 2024-05-08 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0003_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='themes_images'),
        ),
    ]
