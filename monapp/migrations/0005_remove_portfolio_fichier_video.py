# Generated by Django 4.2.11 on 2024-03-19 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monapp', '0004_contact_portfolio_fichier_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='fichier_video',
        ),
    ]
