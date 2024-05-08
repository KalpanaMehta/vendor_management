# Generated by Django 5.0.4 on 2024-05-02 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0002_vendor_average_response_time_vendor_fulfillment_rate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor_Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('on_time_delivery_rate', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('average_response_time', models.FloatField()),
                ('fulfillment_rate', models.FloatField()),
                ('vendor_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor', to_field='vendor_code')),
            ],
        ),
    ]
