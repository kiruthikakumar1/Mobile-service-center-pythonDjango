# Generated by Django 5.0.4 on 2024-04-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0002_alter_product_product_originalprice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odproname', models.CharField(max_length=150)),
                ('odprocolor', models.IntegerField()),
                ('odprostorage', models.IntegerField()),
                ('odproprice', models.CharField(max_length=100)),
                ('odprobattery', models.CharField(max_length=100)),
                ('odproscreen', models.CharField(max_length=100)),
                ('odpronetwork', models.CharField(max_length=100)),
            ],
        ),
    ]
