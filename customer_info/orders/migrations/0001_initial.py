# Generated by Django 3.0.8 on 2020-07-11 04:09

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('credit_cards', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, size=None)),
                ('company_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('order_name', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Customer')),
            ],
        ),
    ]
