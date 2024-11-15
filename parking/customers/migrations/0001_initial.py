# Generated by Django 5.1.3 on 2024-11-13 00:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('registration_date', models.DateField()),
                ('is_regular_customer', models.BooleanField(default=False)),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegularPass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_date', models.DateField()),
                ('start_date', models.DateField()),
                ('duration_in_days', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
    ]
