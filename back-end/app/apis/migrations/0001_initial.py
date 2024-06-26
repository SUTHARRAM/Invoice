# Generated by Django 5.0.4 on 2024-05-05 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientDetail',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=100)),
                ('city_name', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=500)),
                ('pin_code', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('last_modified_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('city_name', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=20)),
                ('pin_code', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('last_modified_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BillDetail',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('last_modified_by', models.CharField(max_length=100)),
                ('fk_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.clientdetail')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.userdetail')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetail',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('last_modified_by', models.CharField(max_length=100)),
                ('fk_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.billdetail')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('rate', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('last_modified_by', models.CharField(max_length=100)),
                ('fk_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.billdetail')),
            ],
        ),
    ]
