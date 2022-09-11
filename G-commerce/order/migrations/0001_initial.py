# Generated by Django 4.0.7 on 2022-08-14 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import order.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('coupon_id', models.CharField(default=order.models.coupon_uid, max_length=20, primary_key=True, serialize=False)),
                ('coupon_type', models.CharField(choices=[['shipping', 'shipping'], ['discount', 'discount']], max_length=50)),
                ('coupon_discount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PickupStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
                ('station', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_type', models.CharField(max_length=20)),
                ('shipping_fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
