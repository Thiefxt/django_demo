# Generated by Django 2.0.13 on 2019-11-11 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_id', models.IntegerField()),
                ('shop_id', models.IntegerField()),
                ('parent_id', models.IntegerField()),
                ('order_sn', models.CharField(max_length=32)),
                ('order_type', models.IntegerField(blank=True, null=True)),
                ('charge_id', models.IntegerField(blank=True, null=True)),
                ('shopping_id', models.IntegerField()),
                ('status', models.IntegerField(blank=True, null=True)),
                ('goods_count', models.IntegerField()),
                ('is_frozen', models.IntegerField()),
                ('from_source', models.IntegerField(blank=True, null=True)),
                ('create_time', models.IntegerField()),
                ('remark', models.CharField(blank=True, max_length=64, null=True)),
                ('resource', models.CharField(blank=True, max_length=128, null=True)),
                ('refund_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'so_order',
            },
        ),
        migrations.CreateModel(
            name='SoOrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=128)),
                ('goods_classify', models.TextField(blank=True, null=True)),
                ('count', models.IntegerField()),
                ('money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_url', models.CharField(blank=True, max_length=128, null=True)),
                ('comment_id', models.IntegerField(blank=True, null=True)),
                ('sf_id', models.IntegerField(blank=True, null=True)),
                ('goods_id', models.IntegerField(blank=True, null=True)),
                ('should_money', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('shop_coupons', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pt_coupons', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'so_order_goods',
            },
        ),
    ]
