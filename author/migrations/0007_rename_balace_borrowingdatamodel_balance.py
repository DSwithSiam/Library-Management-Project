# Generated by Django 5.0.1 on 2024-01-06 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0006_alter_borrowingdatamodel_book_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowingdatamodel',
            old_name='balace',
            new_name='balance',
        ),
    ]
