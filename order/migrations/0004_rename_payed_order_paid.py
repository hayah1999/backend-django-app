# Generated by Django 4.2 on 2023-05-02 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_payed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='payed',
            new_name='paid',
        ),
    ]
