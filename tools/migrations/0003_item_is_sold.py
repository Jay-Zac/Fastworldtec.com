# Generated by Django 5.0.3 on 2024-04-07 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_alter_item_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
    ]