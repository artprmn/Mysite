# Generated by Django 4.2.1 on 2024-02-05 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=10)),
                ('entrances', models.PositiveIntegerField()),
                ('apartments_per_entrance', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('houses', models.ManyToManyField(blank=True, to='myapp.house')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.userprofile')),
            ],
        ),
    ]
