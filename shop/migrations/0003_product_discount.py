# Generated by Django 5.0.1 on 2024-01-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0, verbose_name='Скидка'),
        ),
    ]
