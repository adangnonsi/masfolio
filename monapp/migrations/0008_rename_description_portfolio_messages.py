# Generated by Django 4.2.11 on 2024-03-26 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monapp', '0007_alter_contact_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='description',
            new_name='messages',
        ),
    ]