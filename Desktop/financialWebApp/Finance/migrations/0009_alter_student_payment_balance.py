# Generated by Django 4.0.8 on 2024-04-03 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0008_alter_session_end_date_alter_session_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='payment_balance',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
