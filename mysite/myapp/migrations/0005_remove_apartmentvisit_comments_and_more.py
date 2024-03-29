# Generated by Django 4.2.1 on 2024-02-06 03:26

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_house_campaign_apartmentvisit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentvisit',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='apartmentvisit',
            name='contacts_name',
        ),
        migrations.RemoveField(
            model_name='apartmentvisit',
            name='contacts_phone',
        ),
        migrations.RemoveField(
            model_name='apartmentvisit',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='apartmentvisit',
            name='user',
        ),
        migrations.AddField(
            model_name='apartmentvisit',
            name='apartment_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apartmentvisit',
            name='comment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apartmentvisit',
            name='contact_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apartmentvisit',
            name='contact_phone',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apartmentvisit',
            name='date',
            field=models.DateField(default=datetime.date(2024, 2, 6)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apartmentvisit',
            name='time',
            field=models.TimeField(default=datetime.time(3, 24, 20, 987644)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apartmentvisit',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apartmentvisit',
            name='reaction',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.house')),
            ],
        ),
    ]
