# Generated by Django 5.0.1 on 2024-01-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0004_borrowingdatamodel_useraccount_delete_borrowingmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowingdatamodel',
            name='book_price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
    ]
