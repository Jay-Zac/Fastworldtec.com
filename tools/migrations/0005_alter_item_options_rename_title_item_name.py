# Generated by Django 5.0.3 on 2024-04-15 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0004_remove_item_conclusion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',)},
        ),
        migrations.RenameField(
            model_name='item',
            old_name='title',
            new_name='name',
        ),
    ]