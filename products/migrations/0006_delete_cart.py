# Generated by Django 3.2.8 on 2021-11-10 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]