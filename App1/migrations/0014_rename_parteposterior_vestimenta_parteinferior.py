# Generated by Django 4.2.5 on 2023-10-24 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0013_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vestimenta',
            old_name='parteposterior',
            new_name='parteinferior',
        ),
    ]
