# Generated by Django 3.1 on 2020-08-12 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LogisticForOrder', '0004_courieragency_min_kg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='min_two_kg_rate',
            new_name='min_kg_rate',
        ),
    ]
