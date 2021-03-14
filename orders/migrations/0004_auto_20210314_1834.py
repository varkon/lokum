# Generated by Django 3.0.11 on 2021-03-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210116_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='self_delivery',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.CharField(choices=[('S', 'Pickup'), ('D', 'Delivery')], default='S', max_length=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='Pickup', max_length=250, verbose_name='address'),
        ),
    ]
