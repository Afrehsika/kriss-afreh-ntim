# Generated by Django 4.0.8 on 2024-03-06 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0003_rename_student_fess_levelbill_student_fees_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='Finance.student'),
        ),
    ]
