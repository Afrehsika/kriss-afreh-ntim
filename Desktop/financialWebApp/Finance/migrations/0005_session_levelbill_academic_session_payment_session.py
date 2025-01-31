# Generated by Django 4.0.8 on 2024-03-09 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0004_alter_payment_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=200, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_current_session', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='levelbill',
            name='academic_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finance.session'),
        ),
        migrations.AddField(
            model_name='payment',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finance.session'),
        ),
    ]
