# Generated by Django 5.0.2 on 2024-05-02 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0008_order_oduserfname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='oduserfname',
            field=models.CharField(max_length=150),
        ),
    ]
