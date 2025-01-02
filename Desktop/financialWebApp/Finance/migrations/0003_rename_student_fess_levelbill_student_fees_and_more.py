# Generated by Django 4.0.8 on 2024-03-06 17:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0002_levelbill_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='levelbill',
            old_name='student_fess',
            new_name='student_fees',
        ),
        migrations.AddField(
            model_name='student',
            name='payment_balance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='payment',
            name='bank_of_payment',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paid_amount',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.TextField(max_length=100),
        ),
    ]
