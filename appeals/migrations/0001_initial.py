# Generated by Django 5.2 on 2025-04-04 14:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('appeal_org', models.CharField(choices=[('OrgA', 'Organization A'), ('OrgB', 'Organization B')], max_length=100)),
                ('appointment', models.CharField(max_length=255)),
                ('appointment_type', models.CharField(choices=[('Type1', 'Type 1'), ('Type2', 'Type 2')], max_length=100)),
                ('client_code', models.CharField(max_length=100)),
                ('client_card', models.CharField(max_length=100)),
                ('drop_card', models.CharField(max_length=100)),
                ('appeal_date', models.DateField()),
                ('responsible', models.CharField(max_length=255)),
                ('controller', models.CharField(max_length=255)),
                ('damage', models.IntegerField()),
                ('currency', models.CharField(choices=[('UZS', 'UZS'), ('USD', 'USD'), ('EUR', 'EUR')], max_length=10)),
                ('status', models.CharField(max_length=100)),
                ('measures', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AppealFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='appeal_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('appeal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='appeals.appeal')),
            ],
        ),
    ]
