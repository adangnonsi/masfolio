# Generated by Django 4.2.11 on 2024-03-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monapp', '0006_rename_desciption_contact_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
