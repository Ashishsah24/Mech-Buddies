# Generated by Django 4.1.5 on 2023-04-02 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_customer_support'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_support',
            old_name='comment',
            new_name='Comment',
        ),
    ]
