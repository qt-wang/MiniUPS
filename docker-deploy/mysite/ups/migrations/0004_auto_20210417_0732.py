# Generated by Django 3.1.7 on 2021-04-17 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ups', '0003_auto_20210410_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('truck_id', models.IntegerField(primary_key=True, serialize=False)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('truck_status', models.CharField(choices=[('idle', 'idle'), ('in route to a warehouse', 'in route to a warehouse'), ('invalid', 'invalid'), ('delivering', 'delivering'), ('waiting for pickup', 'waiting for pickup')], default='idle', max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='package',
            name='truck_id',
        ),
        migrations.AlterField(
            model_name='package',
            name='package_status',
            field=models.CharField(choices=[('packing', 'packing'), ('packed', 'packed'), ('loading', 'loading'), ('loaded', 'loaded'), ('delivering', 'delivering'), ('delivered', 'delivered')], default='packing', max_length=30),
        ),
        migrations.AddField(
            model_name='package',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ups.product'),
        ),
        migrations.AddField(
            model_name='package',
            name='truck',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ups.truck'),
        ),
    ]
